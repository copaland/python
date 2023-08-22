Sub CreateSlidesFromExcel()

    Dim pptApp As Object
    Dim pptPresentation As Object
    Dim pptSlide As Object
    Dim pptTextbox As Object
    Dim ExcelApp As Object
    Dim ExcelWorkbook As Object
    Dim ExcelRange As Range
    Dim ExcelCell As Range
    Dim ColumnHeader As String
    Dim LastRow As Long

    ' Excel 초기화
    Set ExcelApp = CreateObject("Excel.Application")
    With ExcelApp
        .Visible = False
        Set ExcelWorkbook = .Workbooks.Open(Application.GetOpenFilename(Title:="Excel 파일 선택", FileFilter:="Excel Files *.xls; *.xlsx"))
        Set ExcelRange = ExcelWorkbook.Sheets(1).Range("A1").EntireColumn ' A열 기준 - 필요하다면 수정하세요.
        ColumnHeader = ExcelRange.Cells(1, 1).Value
        LastRow = ExcelRange.Cells(ExcelRange.Rows.Count, 1).End(xlUp).Row
    End With

    ' PowerPoint 초기화
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = msoTrue
    Set pptPresentation = pptApp.Presentations.Add

    ' Excel 데이터를 기반으로 PowerPoint 슬라이드 생성
    For Each ExcelCell In ExcelRange.Cells
        If ExcelCell.Row <= LastRow Then
            Set pptSlide = pptPresentation.Slides.Add(ExcelCell.Row, 1) ' Title 슬라이드 형식
            Set pptTextbox = pptSlide.Shapes(1) ' 첫 번째 텍스트 박스 선택
            pptTextbox.TextFrame.TextRange.Text = ColumnHeader & ": " & ExcelCell.Value
        End If
    Next ExcelCell

    ' 정리
    ExcelWorkbook.Close
    ExcelApp.Quit
    Set pptSlide = Nothing
    Set pptPresentation = Nothing
    Set pptApp = Nothing
    Set ExcelRange = Nothing
    Set ExcelWorkbook = Nothing
    Set ExcelApp = Nothing

End Sub

