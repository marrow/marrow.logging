from marrow.logging import log

# normal stuff
log.debug("Debugging message.")
log.error("Error level message.")
log.info('{0} is having issues in {where}.', 'GothAlice', where='sector 27')

# renaming
baz = log.name('baz')
baz.debug('Diz!')

# newline handling
log.info('user\ninput\nannoys\nus')
log.options(newlines=False).info('we\ndeal')

# exception handling
try:
    1/0
except:
    log.trace('error', prefix="\n").warning('oh noes')

# additional data
log.data(path="less traveled", roads=42).info('Going for a walk')

# log only fields as data -- no positional arguments
log.info(paths=42, dolphins='thankful')