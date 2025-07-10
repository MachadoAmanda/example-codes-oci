import oci
import base64
      
# Para criar um arquivo de configuração, siga a documentação
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
config = oci.config.from_file("~/.oci/config", "SAOPAULO")
      
# Cliente Vision
ai_vision_client = oci.ai_vision.AIServiceVisionClient(config) 

# Transformando em base64
ocr_image = 'parking-demo2.jpg' # Localização da imagem
with open(ocr_image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

      

analyze_image_response = ai_vision_client.analyze_image(
    analyze_image_details=oci.ai_vision.models.AnalyzeImageDetails(
        features=[
            oci.ai_vision.models.ImageObjectDetectionFeature(
                feature_type="OBJECT_DETECTION", 
                max_results=50
        )],   
        image=oci.ai_vision.models.InlineImageDetails(
            source="INLINE",
            data=encoded_string.decode("utf-8")),
        compartment_id="ocid1.compartment.oc1..aaaaaaaa3x7n7wwfnghe4imvt3niwo76wgqv6ecn2iadiwoph73jjowbhbna"),
    )
      

result = analyze_image_response.data

# Acessa os objetos detectados diretamente como propriedades
for obj in result.image_objects:
    nome = obj.name
    confianca = obj.confidence * 100  
    print(f"{nome}: {confianca:.2f}%")
print("Total de carros: " + str(len(result.image_objects)))
