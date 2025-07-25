# transcription.py
import whisper

_whisper_model = None

def get_whisper_model(model_size="small"):
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model(model_size)
    return _whisper_model

def transcribe_audio(file_path, model_size="small"):
    """
    Transcribe un archivo de audio a texto usando OpenAI Whisper.
    """
    try:
        model = get_whisper_model(model_size)
        result = model.transcribe(file_path, language="es")
        return result["text"]
    except Exception as e:
        print(f"Error al transcribir audio {file_path}: {e}")
        return ""
