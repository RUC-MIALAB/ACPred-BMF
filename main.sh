main_directory=`pwd`
model_type=$1
data_dir="$main_directory/data"
result_dir="$main_directory/result"

if [ ! -d "$result_dir" ]; then
	mkdir $result_dir
else
    cd $result_dir
    chmod u+x *
    rm -rf *
    cd ..
fi

for file in "$data_dir"/*; do
    if [ -f "$file" ]; then
        if [[ "$file" == *.fasta ]]; then
	    filename=$(basename "${file%.*}")
	    if [ $model_type == "main" ]; then
                 python server_code_main.py $file $result_dir $filename
	    elif [ $model_type == "alternative" ]; then
                 python server_code_alternative.py $file $result_dir $filename
	    else
		 echo "Wrong model type!"
            fi 
        fi
fi
done

