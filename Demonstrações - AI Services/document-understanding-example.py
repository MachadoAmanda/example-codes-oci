"""
This python script provides an example of how to use OCI Document Understanding text extraction feature

The configuration file used by service clients will be sourced from the default location (~/.oci/config) and the
CONFIG_PROFILE profile will be used.

The sample attempts to extract text from an inline document
Successful run of this sample will create job results under object storage configured under output_location variable
"""
import oci
import uuid
import base64

# Setup basic variables
# Auth Config
CONFIG_PROFILE = "SAOPAULO"
config = oci.config.from_file('~/.oci/config', CONFIG_PROFILE)

# Compartment where processor job will be created
COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaa3x7n7wwfnghe4imvt3niwo76wgqv6ecn2iadiwoph73jjowbhbna"  

#sample document
file_path = "cnh-demo.jpg"
text_extraction_sample_string = None
with open(file_path, "rb") as document_file:
    text_extraction_sample_string = base64.b64encode(document_file.read()).decode('utf-8')

def create_processor_job_callback(times_called, response):
    print("Waiting for processor lifecycle state to go into succeeded state:", response.data)

aiservicedocument_client = oci.ai_document.AIServiceDocumentClientCompositeOperations(oci.ai_document.AIServiceDocumentClient(config=config))

# Text extraction feature 
text_extraction_feature = oci.ai_document.models.DocumentTextExtractionFeature()

# Setup the output location where processor job results will be created
output_location = oci.ai_document.models.OutputLocation()
output_location.namespace_name = "idajmumkp9ca"  
output_location.bucket_name = "amanda-bucket"  
output_location.prefix = "document_understanding_demo"  

# Create a processor_job for text_extraction feature
create_processor_job_details_text_extraction = oci.ai_document.models.CreateProcessorJobDetails(
                                                    display_name=str(uuid.uuid4()),
                                                    compartment_id=COMPARTMENT_ID,
                                                    input_location=oci.ai_document.models.InlineDocumentContent(data=text_extraction_sample_string),
                                                    output_location=output_location,
                                                    processor_config=oci.ai_document.models.GeneralProcessorConfig(features=[text_extraction_feature]))

#print("Calling create_processor with create_processor_job_details_text_extraction:", create_processor_job_details_text_extraction)
create_processor_response = aiservicedocument_client.create_processor_job_and_wait_for_state(
    create_processor_job_details=create_processor_job_details_text_extraction,
    wait_for_states=[oci.ai_document.models.ProcessorJob.LIFECYCLE_STATE_SUCCEEDED],
    waiter_kwargs={"wait_callback": create_processor_job_callback})

#print("processor call succeeded with status: {} and request_id: {}.".format(create_processor_response.status, create_processor_response.request_id))
processor_job: oci.ai_document.models.ProcessorJob = create_processor_response.data
#print("create_processor_job_details_text_detection response: ", create_processor_response.data)

print("Getting defaultObject.json from the output_location")
object_storage_client = oci.object_storage.ObjectStorageClient(config=config)
get_object_response = object_storage_client.get_object(namespace_name=output_location.namespace_name,
                                                       bucket_name=output_location.bucket_name,
                                                       object_name="{}/{}/_/results/defaultObject.json".format(
                                                           output_location.prefix, processor_job.id))
print(str(get_object_response.data.content.decode()[0:100]))