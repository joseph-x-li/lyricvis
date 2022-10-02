# Linux install
# Conda installs first
# pip installs second
# conda: pytorch, youtube-dl
# pip: diffusers, transformers, youtube-dl, 

echo "DO THIS IN A NEW CONDA ENVIRONMENT!!!!"

conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
conda install -c conda-forge youtube-dl
pip install webvtt-py
pip install gradio
pip install diffusers
pip install transformers
pip install moviepy