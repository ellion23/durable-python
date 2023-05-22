var 
i, j: integer;
count: longint;
maxsum: integer;
arr: array[1..30000] of integer;
f: text;
begin
    assign(f,'/home/ellion/heh/in.txt');
    reset(f);
    maxsum := 0;
    count := 0;
    for i := 1 to 30000 do readln(f, arr[i]);
    for i := 1 to 30000 - 1 do
        for j := i + 1 to 30000 do begin
            if (arr[i] mod 7 = 0) or (arr[j] mod 7 = 0) then
                if (arr[i] mod 160 <> arr[j] mod 160) then begin
                    count := count + 1;
                    if arr[i] + arr[j] > maxsum then maxsum := arr[i] + arr[j];
                end;
        end;
    writeln(count, ' ', maxsum);
end.
