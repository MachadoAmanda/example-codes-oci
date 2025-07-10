import oci
import time
import json

# Configuração OCI
config = oci.config.from_file("~/.oci/config", "SAOPAULO")
compartment_id = "ocid1.compartment.oc1..aaaaaaaa3x7n7wwfnghe4imvt3niwo76wgqv6ecn2iadiwoph73jjowbhbna"
namespace = "idajmumkp9ca"
bucket = "amanda-bucket"
object_name = "demo-audio.wav"
output_prefix = "transcricoes_ORACLE"

# Clientes OCI
object_storage = oci.object_storage.ObjectStorageClient(config)
speech = oci.ai_speech.AIServiceSpeechClient(config)

# Upload do áudio
with open(object_name, 'rb') as f:
    object_storage.put_object(namespace, bucket, object_name, f)

# Criar job de transcrição
job_response = speech.create_transcription_job(
    oci.ai_speech.models.CreateTranscriptionJobDetails(
        compartment_id=compartment_id,
        input_location=oci.ai_speech.models.ObjectListInlineInputLocation(
            location_type="OBJECT_LIST_INLINE_INPUT_LOCATION",
            object_locations=[oci.ai_speech.models.ObjectLocation(
                namespace_name=namespace,
                bucket_name=bucket,
                object_names=[object_name]
            )]
        ),
        output_location=oci.ai_speech.models.OutputLocation(
            namespace_name=namespace,
            bucket_name=bucket,
            prefix=output_prefix
        ),
        display_name="TranscricaoSimples",
        model_details=oci.ai_speech.models.TranscriptionModelDetails(
            model_type="ORACLE", # WHISPER_MEDIUM ou WHISPER_LARGE_V2(sobre requisição)
            domain="GENERIC",
            language_code="pt-BR" # Oracle -> pt-BR, Whisper -> pt
        ),
        normalization=oci.ai_speech.models.TranscriptionNormalization(
            is_punctuation_enabled=True
        )
    )
)

# Esperar até o job finalizar
job_id = job_response.data.id
print(f"Transcrição iniciada (job_id={job_id})...")

while True:
    job = speech.get_transcription_job(job_id).data
    if job.lifecycle_state == "SUCCEEDED":
        break
    elif job.lifecycle_state == "FAILED":
        print("Transcrição falhou.")
        exit()
    time.sleep(1)

# Obter transcrição
objects = object_storage.list_objects(namespace, bucket, prefix=output_prefix)
for obj in objects.data.objects:
    if obj.name.endswith(object_name + ".json"):
        result = object_storage.get_object(namespace, bucket, obj.name)
        data = json.loads(result.data.text)
        texto = data['transcriptions'][0]['transcription']
        confianca = float(data['transcriptions'][0]['confidence']) * 100
        print("\n--- Transcrição ---")
        print(texto)
        print(f"\nConfiança: {confianca:.2f}%")
        break