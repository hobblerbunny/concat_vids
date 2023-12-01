from concat import ConcatFramesNumpy
video_maker = ConcatFramesNumpy

video_maker = ConcatFramesNumpy()
video_maker.output_folder = "video_pelotas"
video_maker.read_frame = "D:/Judson_projetos/frame_save_pelotas/projeto_pelotas/projeto_pelotas_2023-01-11_04/vid_2"
frames = video_maker.read_frame
frames = video_maker.matrix_color(frames, "BGR>RGB")
video = video_maker.convert_vid(frames, fps=5)
video_maker.save(video, "vid_2_2023-01-11_04", data=True)