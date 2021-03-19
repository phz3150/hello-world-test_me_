def displacement(u,t,a):
    """Calculates the total displacement of a body during a time interval t, 
     when the body has initial speed u_init and a constant acceleration a. 
  
     Input: u (m/s), t (sec), a (m/s^2)
     Output: d (m) """


    s= u * t + 0.5 * a * (t**2)
    return(s)