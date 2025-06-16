PROGRAM merge_sort;
{$mode objfpc}

USES crt, SysUtils, fgl;

TYPE
  TIntegerList = specialize TFPGList<Integer>;
  TIntegerArray = array of Integer;


FUNCTION GetNumberList: TIntegerArray;
VAR
  num_list: TIntegerList;
  numbers: TIntegerArray;
  input: string;
  value, i: Integer;

BEGIN
  Clrscr;

  num_list := TIntegerList.Create;
  try
    WriteLn('Please enter a list of numbers, one at a time: ');
    repeat
      Write('> ');
      Readln(input);
      if input = '' then
        Break;
      if TryStrToInt(input, value) then
        num_list.Add(value)
      else
        WriteLn('Invalid Input. Please enter a number.');
    until FALSE;

    //WriteLn('You entered ', num_list.Count, ' numbers:');
    //for i := 0 to num_list.Count -1 do
    //  WriteLn(num_list[i]); // Can't write a TFPG object.
    //WriteLn(num_list)i

    //Allocate Array with exact required size.
    SetLength(numbers, num_list.Count);

   //Copy contents of TFPGList to new array
   for i := 0 to num_list.Count - 1 do
     numbers[i] := num_list[i];

    finally
      num_list.Free;
END;
   
    //WriteLn(numbers); 
    //Cant print an IntArray

PROCEDURE PrintNumberList(const arr: TIntegerArray);
VAR
  i: Integer;
BEGIN
  Write('Your List: ');
  for i := 0 to High(arr) do
  BEGIN
    Write(arr[i]);
    if i < High(arr) then
      Write(', ');
  END;
  WriteLn;
END;


BEGIN
//MAIN

  VAR userNumbers := GetNumberList;
  PrintNumberList(userNumbers);

END.

