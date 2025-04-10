# loop over all files in the pdf directory
for dir in pdf/*;
do
  
  for file in $dir/*;
  do 
      # extract the directory name from the file path
      out_dir=`echo $dir | cut -d '/' -f 2`

      # call the marker_single command with the file as an argument
      # assuming you have an ollama instance running on localhost:11434
      # and the gemma3:12b model is available
      uv run marker_single "$file"  \
        --output_dir ./markdown/$out_dir \
        --ollama_base_url=http://localhost:11434/ \
        --llm_service=marker.services.ollama.OllamaService \
        --ollama_model=gemma3:12b
      
      echo "$file -> markdown/$out_dir"
  done
done