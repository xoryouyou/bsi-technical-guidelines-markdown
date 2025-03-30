# loop over all files in the pdf directory
for file in pdf/*;
do 
    # call the marker_single command with the file as an argument
    # assuming you have an ollama instance running on localhost:11434
    # and the gemma3:12b model is available
    uv run marker_single $file  \
      --output_dir ./markdown \
      --ollama_base_url=http://localhost:11434/ \
      --llm_service=marker.services.ollama.OllamaService \
      --ollama_model=gemma3:12b
done