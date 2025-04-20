# call the marker script to convert all PDFs in the pdf subdirectories to markdown
for dir in pdf/*;
do 
  echo "Processing directory: $dir"
  uv run marker \
    $dir \
    --workers 1 \
    --ollama_base_url=http://localhost:11434/ \
    --llm_service=marker.services.ollama.OllamaService \
    --ollama_model=gemma3:12b
done