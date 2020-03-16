function pointsOfStamina(p, x)
   local points = 0
   for i = 1, #x do
      points = points + (x[i] - p)^2
   end
   return points
end


local n = io.read("*n")
local x = {}

for i = 1, n do
   x[i] = io.read("*n")
end

local min = {coordinate=1, points=pointsOfStamina(1, x)}
for i = 2, 100 do
   local points = pointsOfStamina(i, x)
   if points < min.points then
      min.coordinate = i
      min.points = points
   end
end

print(string.format("%d", min.points))
