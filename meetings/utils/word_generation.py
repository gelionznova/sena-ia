#word_generation.py
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm
from io import BytesIO

def generate_word_acta(context):
    import logging
    logger = logging.getLogger("word_generation")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'templates', 'acta_template.docx')

    doc_tpl = DocxTemplate(template_path)

    anexos = []
    for anexo in context.get("anexos", []):
        try:
            image = InlineImage(doc_tpl, anexo["image_path"], Cm(8))
            anexos.append({
                "filename": anexo["filename"],
                "image": image,
            })
        except Exception as e:
            logger.warning(
                f"No se pudo cargar la imagen '{anexo['filename']}' ({anexo['image_path']}): {e}"
            )
            anexos.append({
                "filename": anexo["filename"],
                "image": None,
                "error": str(e),
            })

    context = context.copy()
    context["anexos"] = anexos

    doc_tpl.render(context)

    output = BytesIO()
    doc_tpl.save(output)
    output.seek(0)
    return output
