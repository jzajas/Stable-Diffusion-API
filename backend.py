import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

PROMPT = (
    "4 dog in mafia suits and sunglasses playing poker in a small room with lamp above their heads as the only source of light"
)

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0",
    # available engines: https://platform.stability.ai/docs/features/api-parameters#engine
)

answers = stability_api.generate(
    prompt=PROMPT,
    style_preset="cinematic",
    seed=0,
    steps=50,
    cfg_scale=8.0,
    width=1024,
    height=1024,
    samples=1,
    sampler=generation.SAMPLER_K_DPMPP_2M,
    # Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral,
    # k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
)

for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save(str(artifact.seed) + ".png")
