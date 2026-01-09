
from oci_openai import OciOpenAI, OciSessionAuth,OciUserPrincipalAuth

client = OciOpenAI(
    region="us-chicago-1",
    auth=OciUserPrincipalAuth(profile_name="CHICAGOV2"), # or OciResourcePrincipalAuth | OciInstancePrincipalAuth | OciUserPrincipalAuth
    compartment_id="ocid1.compartment.oc1..aaaaaaaaev2ipyek53f7sck5ibvtnqrp5w2k54qiuk2cikbfati5bk54yhka", # a compartment of your tenancy that this caller identity has access to
    conversation_store_id="ocid1.generativeaiconversationstore.oc1.us-chicago-1.amaaaaaad6nji3aae6vnp4ultcvmwobd7ungoct3vq7s7g35mzfn22zu6fqq",
)

# the response created will now also persist in the conversation store
response1 = client.responses.create(
    model="openai.gpt-5",
    input="qual meu nome?"
)

print(response1)