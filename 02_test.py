import 02
def test_visualize_height_distribution_from_csv():
    csv_file_path = 'data.csv' 
    box_plot_path, histogram_path = visualize_height_distribution_from_csv(csv_file_path)

    # Test if the files were created
    assert os.path.exists(box_plot_path)
    assert os.path.exists(histogram_path)
