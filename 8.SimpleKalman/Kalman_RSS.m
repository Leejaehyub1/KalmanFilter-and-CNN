function rss = Kalman_RSS(arr)
%
%
persistent A H Q R 
persistent y P
persistent flagRun


if isempty(flagRun)
  A = 1;    % 칼만 필터에서 필요한 parameter를 정의함.(A, H, Q, R)
  H = 1;
  
  Q = 0;
  R = 50;
  
  length = size(arr,2)  % arr 함수의 열의 갯수를 반환
  cut_ratio = 0
  num_of_cut = fix(length * cut_ratio) % 전체 열 갯수 중에서 cut_ratio 비율 만큼 잘라냄.
  
  for a=1:num_of_cut % for문을 돌면서 최대, 최솟값을 없앰
      min_num = min(arr)
      k = find( arr == min_num)
      arr(k(1)) = []
      
      max_num = max(arr)
      k = find( arr == max_num)
      arr(k(1)) = []
  end
  
  y = median(arr, 'all')
  i = find( arr == y)
  arr(i(1)) = []
  arr = [y,arr] % median을 가장 첫번째로 옮김(처음 값이 중요하기 때문에)
  diff = [arr-y] % arr에서 median을 뺀 배열을 diff로 정의함.
  
  P = var(diff)
  flagRun = 1;  
  
end

for z=arr
    xp = A*y;
    Pp = A*P*A' + Q;
    K = Pp*H'*inv(H*Pp*H' + R);
    y = xp + K*(z - H*xp);
    P = Pp - K*H*Pp;

    rss = y;
end
    
