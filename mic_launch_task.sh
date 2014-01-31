
get_micfile
echo $MIC_LD_LIBRARY_PATH > $HOME/MIC_LD_LIBRARY_PATH
ssh `head -n1 micfile.$PBS_JOBID` < $HOME/mic_task.sh
