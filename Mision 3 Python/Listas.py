{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f628e2eb",
   "metadata": {},
   "source": [
    "# Visualisation of COVID protein\n",
    "In previous lesson we performed BLAST query on our covid protein.\n",
    "\n",
    "We can also retrieve the same structural file SARS-CoV-2 from another database PDB (Protein Data Bank). PDB database stores protein records that contain coordinate information of each atom, which we will be using to visualize SARS-CoV-2 protein."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "717662d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# id of protein we are searching for (cp from day 6 lecture)\n",
    "seq_id = \"pdb|6YYT|A\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "37062b82",
   "metadata": {},
   "outputs": [],
   "source": [
    "id = seq_id.split(\"|\")[1] # extract ID so we can download the PDB file from Protein Data Bank database. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "79025c68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'6YYT'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc763a6d",
   "metadata": {},
   "source": [
    "The Protein Data Bank (pdb) file format is a textual file format describing the three-dimensional structures of molecules held in the Protein Data Bank.\n",
    "\n",
    "Download pdb file with wget command:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1be5518a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2021-12-11 17:40:56--  https://files.rcsb.org/download/6YYT.pdb\n",
      "Resolving files.rcsb.org (files.rcsb.org)... 128.6.158.49\n",
      "Connecting to files.rcsb.org (files.rcsb.org)|128.6.158.49|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: unspecified [application/octet-stream]\n",
      "Saving to: ‘6YYT.pdb.1’\n",
      "\n",
      "6YYT.pdb.1              [    <=>             ] 954,91K  1,43MB/s    in 0,7s    \n",
      "\n",
      "2021-12-11 17:40:57 (1,43 MB/s) - ‘6YYT.pdb.1’ saved [977832]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget https://files.rcsb.org/download/6YYT.pdb"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f3ce6de",
   "metadata": {},
   "source": [
    "### Reading PDB file with Biopython\n",
    "Bio.PDB is a Biopython module that focuses on working with crystal structures of biological macromolecules. Among other things, Bio.PDB includes a PDBParser class that produces a Structure object, which can be used to access the atomic data in the file in a convenient manner. \n",
    "\n",
    "More about it in some later video :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "929d0664",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Bio.PDB import PDBParser # PDBParser - parser for pdb files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d0e4d19c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/lanacaldarevic/opt/miniconda3/envs/12daysofbiopython/lib/python3.8/site-packages/Bio/PDB/StructureBuilder.py:89: PDBConstructionWarning: WARNING: Chain A is discontinuous at line 12059.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Structure id=6YYT>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parser = PDBParser()\n",
    "structure = parser.get_structure('6YYT', '6YYT.pdb') # After parsing, we can fetch the protein structure using get_structure .\n",
    "structure"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5487f621",
   "metadata": {},
   "source": [
    "#### Identify the number of chains\n",
    "To identify how many chains this 6YYT covid viral protein has, we use chain.id function which gives us the list of the chains that are present."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e1ad81c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chain ID: A\n",
      "chain ID: B\n",
      "chain ID: C\n",
      "chain ID: D\n",
      "chain ID: P\n",
      "chain ID: Q\n",
      "chain ID: T\n",
      "chain ID: U\n"
     ]
    }
   ],
   "source": [
    "for chain in structure[0]:\n",
    "    print(f'chain ID: {chain.id}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45bd1b61",
   "metadata": {},
   "source": [
    "We see that this viral SARS-CoV-2 polymerase has 8 chains or 8 accessory proteins, represented with single alphabet."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b34b9a2c",
   "metadata": {},
   "source": [
    "It is finally time for us We will use **nglview** which is an IPython/Jupyter widget to interactively view molecular structures and trajectories, to create an interactive visualization of 6YYT SARS-CoV-2 protein."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7c3962f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nglview as nv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c5dc412a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "26c6a6b592514aac94bf4bcea0d2803d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "NGLWidget()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "381a20f60304478b998c415b2429b2c7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Tab(children=(Box(children=(Box(children=(Box(children=(Label(value='step'), IntSlider(value=1, min=-100)), la…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "nv.show_biopython(structure, gui=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dd3c1c0",
   "metadata": {},
   "source": [
    "This is what the 6YYT SARS-CoV-2 protein looks like.\n",
    "- Two helical stands with different shades of blue color are the RNA template strand and its product strand\n",
    "- The bulk of red ribbons is the polymerase which is an enzyme (functional protein) that makes copies of the RNA chain. This polymerase is an attractive target for the antivirals COVID-19 vaccine.\n",
    "- If we flip the molecule, we can see the yellow and orange ribbons, which are the viral proteins that help the polymerase stay on track and copy long portions of the RNA chain."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (biopython-env)",
   "language": "python",
   "name": "12daysofbiopython-env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}