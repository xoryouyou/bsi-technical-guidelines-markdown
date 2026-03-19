
import pymupdf4llm
from pathlib import Path
from tqdm import tqdm

# Base directories
pdf_base = Path("pdf")
markdown_base = Path("markdown")

# Find all PDF files recursively
pdf_files = list(pdf_base.rglob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files to convert\n")

for pdf_file in tqdm(pdf_files, desc="Converting PDFs", unit="file"):
    # Get the relative path from pdf base directory
    rel_path = pdf_file.relative_to(pdf_base)
    
    # Get the subfolder (e.g., "tr" or "grundschutz")
    subfolder = rel_path.parent
    
    # Get the filename without extension
    filename_stem = pdf_file.stem
    
    # Create output directory: markdown/{subfolder}/{filename}/
    output_dir = markdown_base / subfolder / filename_stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Output file path: markdown/{subfolder}/{filename}/{filename}.md
    output_file = output_dir / f"{filename_stem}.md"
    
    print(f"Converting {rel_path} -> {output_file}")
    
    try:
        # Convert PDF to markdown with images in the same directory
        md_text = pymupdf4llm.to_markdown(
            str(pdf_file),
            write_images=True, # we want the images next to the markdown file
            image_path=str(output_dir)
        )
        
        # Save as UTF8-encoded file
        output_file.write_bytes(md_text.encode())
        
    except Exception as e:
        print(f"Failed converting PDF {rel_path} \nError: {e}\n")

print("Conversion complete!")