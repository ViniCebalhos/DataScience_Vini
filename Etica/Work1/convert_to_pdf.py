#!/usr/bin/env python3
"""
Script para converter Markdown para PDF
Tenta múltiplas abordagens
"""

import sys
import os

def convert_with_pypandoc():
    """Tenta converter usando pypandoc"""
    try:
        import pypandoc
        input_file = 'Analise_Caso_Itau_CRISP.md'
        output_file = 'Analise_Caso_Itau_CRISP.pdf'
        
        pypandoc.convert_file(
            input_file,
            'pdf',
            outputfile=output_file,
            extra_args=['--pdf-engine=pdflatex', '-V', 'geometry:margin=2.5cm']
        )
        print(f"PDF criado com sucesso: {output_file}")
        return True
    except Exception as e:
        print(f"Erro com pypandoc: {e}")
        return False

def convert_with_markdown_weasyprint():
    """Tenta converter usando markdown + weasyprint"""
    try:
        import markdown
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        input_file = 'Analise_Caso_Itau_CRISP.md'
        output_file = 'Analise_Caso_Itau_CRISP.pdf'
        
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Converter markdown para HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        # Adicionar estilo básico
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3 {{
                    color: #333;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 3px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
        {html_content}
        </body>
        </html>
        """
        
        HTML(string=html_with_style).write_pdf(output_file)
        print(f"PDF criado com sucesso: {output_file}")
        return True
    except Exception as e:
        print(f"Erro com markdown+weasyprint: {e}")
        return False

def convert_with_markdown_pdfkit():
    """Tenta converter usando markdown + pdfkit"""
    try:
        import markdown
        import pdfkit
        
        input_file = 'Analise_Caso_Itau_CRISP.md'
        output_file = 'Analise_Caso_Itau_CRISP.pdf'
        
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
        
        html_with_style = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
                h1, h2, h3 {{ color: #333; }}
                code {{ background-color: #f4f4f4; padding: 2px 4px; }}
                pre {{ background-color: #f4f4f4; padding: 10px; }}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        """
        
        pdfkit.from_string(html_with_style, output_file)
        print(f"PDF criado com sucesso: {output_file}")
        return True
    except Exception as e:
        print(f"Erro com markdown+pdfkit: {e}")
        return False

if __name__ == '__main__':
    print("Tentando converter Markdown para PDF...")
    
    # Tenta diferentes métodos
    if convert_with_pypandoc():
        sys.exit(0)
    elif convert_with_markdown_weasyprint():
        sys.exit(0)
    elif convert_with_markdown_pdfkit():
        sys.exit(0)
    else:
        print("\nNenhum método de conversão disponível.")
        print("Tente instalar uma das opções:")
        print("  pip install pypandoc")
        print("  pip install markdown weasyprint")
        print("  pip install markdown pdfkit")
        print("\nOu use pandoc diretamente:")
        print("  pandoc Analise_Caso_Itau_CRISP.md -o Analise_Caso_Itau_CRISP.pdf")
        sys.exit(1)

