Option Explicit
' PPT를 여백없이 2페이지씩 pdf로 변환하는 VBA
' Alt+F11
Sub SaveSlidesAsPDF()

    Dim OriginalPPT As Presentation
    Dim NewPPT As Presentation
    Dim NewSlide As Slide
    Dim OriginalSlide As Slide
    Dim ExportedShape As Shape
    Dim SlideCount As Integer
    Dim i As Integer, j As Integer
    Dim SW As Single, SH As Single
    Dim FileName As String
    Dim TopMargin As Single
    Dim SlideMargin As Single
    
    ' 상단 여백 설정
    TopMargin = 50 '상단 여백을 50 포인트로 설정
    ' 슬라이드와 슬라이드 사이의 여백 설정
    SlideMargin = 80 '슬라이드와 슬라이드 사이의 여백을 80 포인트로 설정
    
    ' 현재 작업중인 프리젠테이션
    Set OriginalPPT = ActivePresentation
    
    ' 새 프리젠테이션 생성
    Set NewPPT = Presentations.Add
    With NewPPT.PageSetup
        .SlideSize = ppSlideSizeA4Paper
        .SlideOrientation = msoOrientationVertical
        SW = .SlideWidth
        SH = .SlideHeight
    End With
    
    SlideCount = OriginalPPT.Slides.Count
    
    For i = 1 To SlideCount Step 2
        ' 새 슬라이드 추가
        Set NewSlide = NewPPT.Slides.Add(j + 1, ppLayoutBlank)
        j = j + 1
        
        ' 원본 슬라이드 복사 및 붙여넣기
        For Each OriginalSlide In OriginalPPT.Slides
            If OriginalSlide.SlideIndex = i Or OriginalSlide.SlideIndex = i + 1 Then
                OriginalSlide.Copy
                Set ExportedShape = NewSlide.Shapes.Paste()(1)
                ExportedShape.LockAspectRatio = msoFalse
                
                If OriginalSlide.SlideIndex Mod 2 = 0 Then
                    ExportedShape.Top = SW / 2 + TopMargin + SlideMargin
                Else
                    ExportedShape.Top = TopMargin
                End If
                ExportedShape.Left = 0 ' 0 촤측 여백을 10 포인트로 설정
                ExportedShape.Width = SW

            End If
        Next OriginalSlide
    Next i
    
    ' PDF로 저장
    FileName = OriginalPPT.Path & "\" & Left(OriginalPPT.Name, InStrRev(OriginalPPT.Name, ".") - 1) & "_converted.pdf"
    NewPPT.SaveAs FileName, ppSaveAsPDF
    
    ' 새 프리젠테이션 닫기
    NewPPT.Close
    
    MsgBox "PDF 저장이 완료되었습니다!", vbInformation, "완료"

End Sub


