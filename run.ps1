$errorActionPreference = 'stop'
$StartTime = $(get-date)
echo "`nš Started at: $StartTime`n"
echo "āØ Apply film grain"
conda activate perfectgrain
python ./add_filter.py in out 'filters/Ilford HP5.jpg' 170
$elapsedTime = $(get-date) - $StartTime
$totalTime = "{0:HH:mm:ss}" -f ([datetime]$elapsedTime.Ticks)
echo "`nš Finished at: $(get-date)"
echo "`nā Elapsed time: $totalTime`n"