$errorActionPreference = 'stop'
$StartTime = $(get-date)
echo "`n🕑 Started at: $StartTime`n"
echo "✨ Apply film grain"
conda activate perfectgrain
python ./add_filter.py in out 'filters/Ilford HP5.jpg' 170
$elapsedTime = $(get-date) - $StartTime
$totalTime = "{0:HH:mm:ss}" -f ([datetime]$elapsedTime.Ticks)
echo "`n🕑 Finished at: $(get-date)"
echo "`n⌛ Elapsed time: $totalTime`n"