from google.cloud import texttospeech

def ssml_to_mp3(ssml_text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Minimal voice — we use Wavenet directly in SSML
    voice_params = texttospeech.VoiceSelectionParams(
        language_code="ru-RU"
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice_params,
        audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"✅ MP3 file saved: {output_file}")

# === ENTER YOUR SSML HERE ===
ssml = """
<speak>
<voice name="ru-RU-Wavenet-A">Я поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">I put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Я не поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">I didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Я поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did I put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда я поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did I put?</voice><break time="3s"/>

<voice name="ru-RU-Wavenet-A">Ты поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">You put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Ты не поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">You didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Ты поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did you put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда ты поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did you put?</voice><break time="3s"/>

<voice name="ru-RU-Wavenet-A">Она поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">She put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Она не поставила</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">She didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Она поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did she put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда она поставила?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did she put?</voice><break time="3s"/>

<voice name="ru-RU-Wavenet-A">Мы поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">We put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Мы не поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">We didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Мы поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did we put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда мы поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did we put?</voice><break time="3s"/>

<voice name="ru-RU-Wavenet-A">Вы поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">You put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Вы не поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">You didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Вы поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did you put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда вы поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did you put?</voice><break time="3s"/>

<voice name="ru-RU-Wavenet-A">Они поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">They put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Они не поставили</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">They didn’t put</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Они поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Did they put?</voice><break time="3s"/>
<voice name="ru-RU-Wavenet-A">Куда они поставили?</voice><break time="3s"/>
<voice name="en-US-Wavenet-D">Where did they put?</voice><break time="3s"/>
</speak>
"""


ssml_to_mp3(ssml, "put.mp3")