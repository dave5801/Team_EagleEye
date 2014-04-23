clear 
clc

azDeg = 20
elDeg = 90
z = .001

if (azDeg > 360)
    azDeg = azDeg - 360;
end

elevAccel = 10 * (pi/180);
rollAccel = 0* (pi/180);

% if (elDeg + elevAccel * (180/pi)) > 90
%     
%    azDeg = azDeg + 180;
%    
%    elDeg = 90 - abs(elDeg -90)
%    
% end
%  
desiredAz = azDeg * (pi/180);
desiredEl = elDeg * (pi/180);
desiredZ = z ;

desiredDeg = [azDeg, elDeg, z];
[desXCart, desYCart, desZCart] = sph2cart(desiredAz,desiredEl, desiredZ);

desiredCart = [desXCart,desYCart,desZCart]';




dcm = angle2dcm(0, rollAccel,elevAccel , 'ZXY');



projMat = dcm * desiredCart;

[proj2sphAz,proj2sphEl,proj2sphZ] = cart2sph(projMat(1), projMat(2), projMat(3))

newSphCoords = [proj2sphAz, proj2sphEl, proj2sphZ];

newSphCoordsDeg = newSphCoords .* (180/pi)


% %%%%%%%%%%%%
% if (newSphCoords(1) > 90 * (pi/180)) && (newSphCoords(1) <= 180* (pi/180))
%     
%     newSphCoords(2) = 90 *(pi/180) + (90 -  newSphCoordsDeg(2))*(pi/180);
%     
% end
% %%%%%%%%%%


if (newSphCoords(1) < (desiredAz + pi +0.001)) && (newSphCoords(1) > (desiredAz + pi  - 0.001))
    newSphCoords(1) = newSphCoords(1) - pi;
    newSphCoords(2) = (pi/2) + ((pi/2) - newSphCoords(2));
end
if (newSphCoords(1) > (desiredAz - pi -0.001)) && (newSphCoords(1) < (desiredAz - pi  + 0.001))
    newSphCoords(1) = newSphCoords(1) + pi;
    newSphCoords(2) = (pi/2) + ((pi/2) - newSphCoords(2));
end
diffSphCoords = newSphCoords - [desiredAz, desiredEl, desiredZ];

diffSphCoordsDeg = diffSphCoords .* (180/pi)

% if newSphCoords(2)*(180/pi) < elDeg
%     
%     diffSphCoordsDeg(2) =  (diffSphCoordsDeg(2) * -1);
%     
% end
      
newCoordToUse = desiredDeg - diffSphCoordsDeg

%%%
for i = 1:length(newCoordToUse)
    
  
    if newCoordToUse(i) > 360 
        newCoordToUse(i) = newCoordToUse(i) - 360
        
        if newCoordToUse(i) > 360 
        newCoordToUse(i) = newCoordToUse(i) - 360
        
        end
        
    end
    
    if newCoordToUse(i) < 0 
        newCoordToUse(i) = newCoordToUse(i) + 360
        
        if newCoordToUse(i) < 0 
        newCoordToUse(i) = newCoordToUse(i) + 360
        
        end
        
    end
    
    if (newCoordToUse(i) > 359.999) && (newCoordToUse(i) < 360.001)
        
        newCoordToUse(i) = 0
    end
        
end
        
%%%%

        
        
        

