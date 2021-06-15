include "globals.mzn";


int: total_edges;
int: total_vertices;
set of int: vertices_indices = 1..total_vertices;
array[vertices_indices, vertices_indices] of int: graph ;
array[vertices_indices, vertices_indices] of var int: colored_edges;
array[vertices_indices] of var int: colored_vertices;
                  
constraint forall(i in 1..total_vertices, j in 1..total_vertices, color=(i + j - 2) mod (total_edges+1))(
                  if graph[i,j] == 1 then 
                    colored_vertices[i] = i -1  /\
                    colored_edges[i,j] = color /\
                    count(k in array1d(1..total_vertices*total_vertices, colored_edges))(k=color) <= 2
                  else
                  colored_edges[i,j] = 0
                  endif
                  );

solve satisfy;
