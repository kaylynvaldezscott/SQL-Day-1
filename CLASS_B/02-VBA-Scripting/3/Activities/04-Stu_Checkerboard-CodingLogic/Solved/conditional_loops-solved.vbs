Sub conditional_loops()

    ' Create a for loop from 1 to 10
    For i = 1 To 10
        Cells(i, 1).Value = i

        ' Use the modulus function to determine if a number is divisible by 2 (even number)
        If Cells(i, 1).Value Mod 2 = 0 Then

            ' Enter "Even Row" the adjacent cell
            Cells(i, 2).Value = "Even Row"
            
        ' If the number is not divisible by 2 (odd number)
        Else

            ' Enter "Even Row" the adjacent cell
            Cells(i, 2).Value = "Odd Row"
            
        ' Close the If/Else Statement
        End If

    Next i

End Sub
Sub CheckerboardAlternateSolution()
    Dim r, c As Integer
    
    For r = 1 To 8
        For c = 1 To 8
            If (r + c) Mod 2 = 0 Then
                Cells(r, c).Interior.ColorIndex = 1 ' Black
            Else
                Cells(r, c).Interior.ColorIndex = 3 ' Red
            End If
        Next c
    Next r
End Sub
