def caught_speeding(speed, is_birthday):
   
  if is_birthday:
    speeding = speed - 5
  else:
      speeding = speed
  
  if speeding > 80:
    return "big ticket"
  elif speeding > 60:
    return 'small ticket'
  else:
    return 'No Ticket'
