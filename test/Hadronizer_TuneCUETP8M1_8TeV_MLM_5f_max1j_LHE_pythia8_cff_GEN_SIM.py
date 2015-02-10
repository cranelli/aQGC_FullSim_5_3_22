# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(25)
)

# Input source
process.source = cms.Source("PoolSource",
			    secondaryFileNames = cms.untracked.vstring(),
			    fileNames = cms.untracked.vstring('file:LM3_Reweight_step0.root')
			    #fileNames = cms.untracked.vstring('file:step0.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_cff nevts:1000'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:LM3_Reweight_step1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
			 maxEventsToPrint = cms.untracked.int32(1),
			 pythiaPylistVerbosity = cms.untracked.int32(1),
			 filterEfficiency = cms.untracked.double(1.0),
			 pythiaHepMCVerbosity = cms.untracked.bool(False),
			 comEnergy = cms.double(8000.),
			 PythiaParameters = cms.PSet(
	pythia8CommonSettingsBlock,
	pythia8CUEP8M1SettingsBlock,
	processParameters = cms.vstring(
	'JetMatching:setMad = off',
	'JetMatching:scheme = 1',
	'JetMatching:merge = on',
	'JetMatching:jetAlgorithm = 2',
	'JetMatching:etaJetMax = 5.',
	'JetMatching:coneRadius = 1.',
	'JetMatching:slowJetPower = 1',
	'JetMatching:qCut = 30.', #this is the actual merging scale
	'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
	'JetMatching:nJetMax = 1', #number of partons in born matrix element for highest multiplicity
	'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
	),
	parameterSets = cms.vstring('pythia8CommonSettings',
				    'pythia8CUEP8M1Settings',
				    'processParameters',
				    )
	)
			 )

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

