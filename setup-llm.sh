# if needed https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python

pip install gpt4all

git clone --recurse-submodules https://github.com/nomic-ai/gpt4all.git
cd gpt4all/gpt4all-backend/
mkdir build
cd build
cmake ..
cmake --build . --parallel  # optionally append: --config Release

cd ../../gpt4all-bindings/python
pip3 install -e .
