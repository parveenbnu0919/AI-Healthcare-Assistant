from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(name, age, gender,
                    disease, description,
                    precautions):

    pdf = SimpleDocTemplate("static/Health_Report.pdf")

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("AI Healthcare Assistant",
                  styles['Title'])
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(f"Patient Name: {name}",
                  styles['Normal'])
    )

    content.append(
        Paragraph(f"Age: {age}",
                  styles['Normal'])
    )

    content.append(
        Paragraph(f"Gender: {gender}",
                  styles['Normal'])
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph(f"Disease: {disease}",
                  styles['Heading2'])
    )

    content.append(
        Paragraph(description,
                  styles['Normal'])
    )

    content.append(Spacer(1,12))

    content.append(
        Paragraph("Precautions",
                  styles['Heading2'])
    )

    for item in precautions:
        content.append(
            Paragraph("• " + item,
                      styles['Normal'])
        )

    pdf.build(content)