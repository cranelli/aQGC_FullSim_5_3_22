# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step0 --conditions auto:startup -s NONE --eventcontent RAWSIM --datatier GEN --filein file:my_lhe.lhe --fileout file:step0.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHESIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('HLTrigger.Configuration.HLT_7E33v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('root://eoscms.cern.ch//eos/cms/store/user/cranelli/lhe_files/LM3_Reweight.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('step0123 nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)






# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:LM3_Reweight_step0123.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_5_2_1/RelValMinBias/GEN-SIM/START52_V4-v1/0002/5A081FCB-6772-E111-9623-0025B3244166.root', \
'/store/relval/CMSSW_5_2_1/RelValMinBias/GEN-SIM/START52_V4-v1/0003/4C958749-9872-E111-A747-003048F1183E.root'])

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7N::All', '')
process.genstepfilter.triggerConditions=cms.vstring("generation_step")

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
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step)
process.schedule.extend([process.digitisation_step,process.L1simulation_step,process.digi2raw_step])
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step])
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# filter all path with the production filter sequence                              
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq

# customisation of the process.                                                                                                     

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC                                   
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC                           
process = customizeHLTforMC(process)




