## LoL-eSports OCR
Since Vanguard appeared in League of Legends, all projects based on reading memory processes have been discontinued due to the difficulties this presents.

Some useful data for eSports streams, such as team gold, is not directly available through the In-Game API.

This software aims to retrieve the gold data using OCR (Optical Character Recognition) from the top header in the League of Legends spectator mode.

Additional data could be gathered on the future

### How it Works
1. A screenshot of the entire main screen is taken every X seconds.
2. The screenshot is cropped to extract two rectangles: one for the red team’s gold and one for the blue team’s gold.
3. OCR algorithms provided by pytesseract are used to extract the gold values.
4. If the extracted gold values for both teams are valid, a GET request is made to the in-game API to retrieve the current timestamp.
5. A record is added to the database with the timestamp, red team gold, and blue team gold.


### Next Steps
- [ ] Reduce the hardcoded settings.
- [ ] Provide a UI interface that renders a gold graph when it recieves a GET request.
- [ ] Add adittional data from API to get make a more complex game status track.

### Requirements
- [Tesserat 5.4.0](https://github.com/UB-Mannheim/tesseract/wiki)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Python modules](./requirements.txt)

### Known Limitations
- Since the crop areas of the interface are hardcoded, the software will, by default, only be able to retrieve data from a 1920x1080 screen resolution in Full Screen or Borderless mode.

