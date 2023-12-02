import io
import os
from google.cloud import texttospeech

def synthesize_text(input_text, output_filename="output.mp3"):

    # Set environment variable for Google Cloud credentials
    credentials_path = "arcane-boulder-404003-8a768e21b658.json"
    print("Full path to credentials:", os.path.abspath(credentials_path))

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "arcane-boulder-404003-8a768e21b658.json"
    # Initialize the Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file to be returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the response's audio content to an output file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_filename}"')

# Example usage
synthesize_text("Please say 'Visualization' to start visualizing your data.")
