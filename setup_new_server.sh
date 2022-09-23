mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

conda create -n eqt python=3.7
conda activate eqt
pip install obspy
pip install EQTransformer

pip install protobuf==3.20.0
git clone https://github.com/smousavi05/EQTransformer.git