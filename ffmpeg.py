import subprocess

video_path = "Everyone_Can_Be_Rich.mp4"
audio_path = video_path[:-4] + ".mp3" 
muted_video_path = 'muted_video.mp4'
output_path = 'output_video.mp4'

# Convert video to audio
def audio_extraction(video_path, audio_path):
    subprocess.run([
        'ffmpeg', '-i', video_path, '-q:a', '0', audio_path
    ])

# Mute original video
def mute(video_path, muted_video_path):
    
    subprocess.run([
        'ffmpeg', '-i', video_path, 
        '-an', muted_video_path
    ])

# Combine muted video and audio files
def add_audio_track(muted_video_path, audio_path):
    output_path = 'output.mp4'
    subprocess.run([
        'ffmpeg', 
        '-i', muted_video_path,
        '-i', audio_path,
        '-c', 'copy',
        output_path
    ])

audio_extraction(video_path,audio_path)
mute(video_path, muted_video_path)
add_audio_track(muted_video_path, 'x.mp3')
