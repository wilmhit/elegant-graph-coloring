include "globals.mzn";


int: total_edges;
int: total_vertices;
set of int: vertices_indices = 0..total_vertices - 1;
array[vertices_indices, vertices_indices] of int: graph ;
array[vertices_indices, vertices_indices] of var int: colored_edges;
array[vertices_indices] of var 0..total_edges: colored_vertices;

constraint alldifferent(colored_vertices); 
constraint forall(i in 0..total_vertices - 1, j in 0..total_vertices - 1, 
                  color=(colored_vertices[i] + colored_vertices[j]) mod (total_edges + 1))(
                  if graph[i,j] == 1 then 
                    colored_edges[i,j] = color /\
                    colored_edges[j,i] = colored_edges[i,j] /\
                    count(colored_edges, colored_edges[i,j], 2)
                  else
                  colored_edges[i,j] = 0
                  endif
                  );
solve satisfy;
