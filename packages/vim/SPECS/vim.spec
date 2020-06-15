%define patchlevel 2102
%define WITH_SELINUX 0
%define desktop_file 0
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 0

%define withvimspell 0
%define withhunspell 0
%define withruby 0
%define withlua 1

%define baseversion 8.1
%define vimdir vim81

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 4%{?dist}
License: Vim and MIT
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}-%{patchlevel}.tar.bz2
Source1: vim.sh
Source2: vim.csh
Source4: virc
Source5: vimrc
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
%if %{withvimspell}
Source13: vim-spell-files.tar.bz2
%endif
Source14: spec-template.new
Source15: macros.vim
#Source17: ftplugin-spec.vim
#Source18: syntax-spec.vim

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-7.4-specsyntax.patch
%if %{withhunspell}
Patch2011: vim-7.0-hunspell.patch
BuildRequires: hunspell-devel
%endif

Patch3000: vim-7.4-syntax.patch
Patch3002: vim-7.4-nowarnings.patch
Patch3004: vim-7.0-rclocation.patch
Patch3006: vim-7.4-checkhl.patch
Patch3007: vim-7.4-fstabsyntax.patch
Patch3008: vim-7.4-syncolor.patch
Patch3010: vim-7.3-manpage-typo-668894-675480.patch
Patch3011: vim-manpagefixes-948566.patch
Patch3013: vim-7.4-globalsyntax.patch
Patch3014: vim-7.4-releasestring-1318991.patch
Patch3016: vim-8.0-copy-paste.patch
# migrate shebangs in script to /usr/bin/python3 and use python2 when necessary
Patch3017: vim-python3-tests.patch
# fips warning
Patch3018: vim-crypto-warning.patch

# gcc is no longer in buildroot by default
BuildRequires: gcc

BuildRequires: python3-devel ncurses-devel gettext perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::Embed) perl(ExtUtils::ParseXS)
#BuildRequires: libacl-devel gpm-devel autoconf file
BuildRequires: autoconf file
%if %{WITH_SELINUX}
BuildRequires: libselinux-devel
%endif
%if "%{withruby}" == "1"
BuildRequires: ruby-devel ruby
%endif
%if "%{withlua}" == "1"
BuildRequires: lua-devel
%endif
%if %{desktop_file}
# for /usr/bin/desktop-file-install
Requires: desktop-file-utils
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 2
Conflicts: filesystem < 3

# vim bundles libvterm, which is used during build - so we need to provide
# bundled libvterm for catching possible libvterm CVEs
Provides: bundled(libvterm)


%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Conflicts: man-pages-fr < 0.9.7-14
Conflicts: man-pages-it < 0.3.0-17
Conflicts: man-pages-pl < 0.24-2
Requires: %{name}-filesystem
Conflicts: %{name}-minimal < %{epoch}:8.1.1-1

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

# Here's a terminator

%package spell
Summary: The dictionaries for spell checking. This package is optional
Requires: vim-common = %{epoch}:%{version}-%{release}

%description spell
This subpackage contains dictionaries for vim spell checking in
many different languages.

%package minimal
Summary: A minimal version of the VIM editor
Provides: vi
Provides: %{_bindir}/vi
# conflicts in package because of manpage move (bug #1599663)
Conflicts: %{name}-common < %{epoch}:8.1.1-1

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, providing
the commands vi, view, ex, rvi, and rview. NOTE: The online help is
only available when the vim-common package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Requires: vim-common = %{epoch}:%{version}-%{release} which
Provides: vim
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/vim
# suggest python3, python2, lua, ruby and perl packages because of their 
# embedded functionality in Vim/GVim
Suggests: python3 python3-libs
Suggests: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version)) perl-devel
%if "%{withruby}" == "1"
Suggests: ruby-libs ruby
%endif
%if "%{withlua}" == "1"
Suggests: lua-libs
%endif

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%package filesystem
Summary: VIM filesystem layout
BuildArch: noarch

%Description filesystem
This package provides some directories which are required by other
packages that add vim files, p.e.  additional syntax files or filetypes.

%package X11
Summary: The VIM version of the vi editor for the X Window System - GVim
# needed in configure script to have correct macros enabled for GUI (#1603272)
#BuildRequires: gtk3-devel
#BuildRequires: libX11-devel
#BuildRequires: libSM-devel
#BuildRequires: libXt-devel
#BuildRequires: libXpm-devel
#BuildRequires: libICE-devel

#Requires: vim-common = %{epoch}:%{version}-%{release} libattr >= 2.4 gtk3 
Requires: vim-common = %{epoch}:%{version}-%{release}
Provides: gvim
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/gvim
#BuildRequires: gtk3-devel libSM-devel libXt-devel libXpm-devel libappstream-glib
#Requires: hicolor-icon-theme
# suggest python3, python2, lua, ruby and perl packages because of their 
# embedded functionality in Vim/GVim
Suggests: python3 python3-libs
Suggests: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version)) perl-devel
%if "%{withruby}" == "1"
Suggests: ruby-libs ruby
%endif
%if "%{withlua}" == "1"
Suggests: lua-libs
%endif

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support by command gvim.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.

%prep
%setup -q -b 0 -n %{vimdir}

# use %%{__python3} macro for defining shebangs in python3 tests
sed -i -e 's,/usr/sgug/bin/python3,%{__python3},' %{PATCH3017}

# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%if %{withhunspell}
%patch2011 -p1
%endif
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# install spell files
%if %{withvimspell}
%{__tar} xjf %{SOURCE13}
%endif

%patch3000 -p1
%patch3002 -p1
%patch3004 -p1
%patch3006 -p1
%patch3007 -p1 -b .fstabsyntax
%patch3008 -p1 -b .syncolor
%patch3010 -p1
%patch3011 -p1
%patch3013 -p1
%patch3014 -p1
%patch3016 -p1
%patch3017 -p1
%patch3018 -p1

%build
%if 0%{?rhel} > 7
export RHEL_ALLOW_PYTHON2_FOR_BUILD=1
%endif

cd src
autoconf

sed -e "s+VIMRCLOC	= \$(VIMLOC)+VIMRCLOC	= %{_prefix}/etc+" Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile

export CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

%if 0%{?fedora} > 31
export LDFLAGS="%{build_ldflags} $(python3-config --libs --embed)"
%else
export LDFLAGS="%{build_ldflags} $(python3-config --libs)"
%endif

cp -f os_unix.h os_unix.h.save
cp -f ex_cmds.c ex_cmds.c.save

# Rewrite to include our lib32
perl -pi -e "s|lib64 lib|lib64 lib32 lib|g" configure.ac
perl -pi -e "s|lib64 lib|lib64 lib32 lib|g" configure.in
perl -pi -e "s|lib64 lib|lib64 lib32 lib|g" configure

# Configure options:
# --enable-fail-if-missing - we need to fail if configure options aren't satisfied
# --with-features - for setting how big amount of features is enabled
# --enable-multibyte - enabling multibyte editing support - for editing files in languages, which one character
#                      cannot be represented by one byte - Asian languages, Unicode
# --disable-netbeans - disabling socket interface for integrating Vim into NetBeans IDE
# --enable-selinux - enabling selinux support
# --enable-Ninterp - enabling internal interpreter
# --with-x - yes if we want X11 support (graphical Vim for X11)
# --with-tlib - which terminal library to use
# --disable-gpm - disabling support for General Purpose Mouse - Linux mouse daemon

export LIBS="-ltinfo"
export LUA_PREFIX=%{_prefix}

perl -pi -e "s/vimrc/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@redhat.com>" \
  --with-modified-by="<bugzilla@redhat.com>" \
  --enable-fips-warning \
  --enable-fail-if-missing

make VIMRCLOC=%{_prefix}/etc VIMRUNTIMEDIR=%{_prefix}/share/vim/%{vimdir} %{?_smp_mflags}
cp vim minimal-vim
make clean

mv -f os_unix.h.save os_unix.h
mv -f ex_cmds.c.save ex_cmds.c

# More configure options:
# --enable-xim - enabling X Input Method - international input module for X,
#                it is for multibyte languages in Vim with X
# --enable-termtruecolor - use terminal with true colors

# Needed to get the braindead vim configure to find sgug motif
export MOTIFHOME=%{_prefix}

%configure --with-features=huge \
  --enable-perlinterp=dynamic \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --with-tlib=ncurses \
  --enable-fips-warning \
  --with-compiledby="<sgug@localhost>" --enable-cscope \
  --with-modified-by="<sgug@localhost>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp=dynamic \
%else
  --disable-rubyinterp \
%endif
%if "%{withlua}" == "1"
  --enable-luainterp=dynamic \
%else
  --disable-luainterp \
%endif
  --enable-python3interp=dynamic \
  --enable-fail-if-missing \
  --enable-motif-check --enable-gui=motif \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir}

#  --enable-gtk3-check --enable-gui=gtk3 \ #

make VIMRCLOC=%{_prefix}/etc VIMRUNTIMEDIR=%{_prefix}/share/vim/%{vimdir} %{?_smp_mflags}
cp vim gvim
make clean

export LIBS="-lintl -ltinfo -liconv"

%configure --prefix=%{_prefix} --with-features=huge \
 --enable-python3interp=dynamic \
 --enable-perlinterp=dynamic \
 --disable-tclinterp \
 --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<sgug@localhost>" \
 --with-tlib=ncurses \
 --enable-fips-warning \
 --with-compiledby="<sgug@localhost>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp=dynamic \
%else
  --disable-rubyinterp \
%endif
%if "%{withlua}" == "1"
  --enable-luainterp=dynamic \
%else
  --disable-luainterp \
%endif
  --enable-fail-if-missing

make VIMRCLOC=%{_prefix}/etc VIMRUNTIMEDIR=%{_prefix}/share/vim/%{vimdir} %{?_smp_mflags}
cp vim enhanced-vim

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE14} %{buildroot}/%{_datadir}/%{name}/vimfiles/template.spec
cp runtime/doc/uganda.txt LICENSE
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
# Adding STRIP=/bin/true, because Vim wants to strip the binaries by himself
# and put the stripped files into correct dirs. Build system (koji/brew) 
# does it for us, so there is no need to do it in Vim
make install DESTDIR=%{buildroot} BINDIR=%{_bindir} VIMRCLOC=%{_prefix}/etc VIMRUNTIMEDIR=%{_prefix}/share/vim/%{vimdir} STRIP=/bin/true
make installgtutorbin  DESTDIR=%{buildroot} BINDIR=%{_bindir} VIMRCLOC=%{_prefix}/etc VIMRUNTIMEDIR=%{_prefix}/share/vim/%{vimdir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 minimal-vim %{buildroot}%{_bindir}/vi
install -m755 enhanced-vim %{buildroot}%{_bindir}/vim
install -m755 gvim %{buildroot}%{_bindir}/gvim
install -p -m644 %{SOURCE7} \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE8} \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE9} \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE10} \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gvim.png
#cp -f %{SOURCE17} %{buildroot}/%{_datadir}/%{name}/%{vimdir}/ftplugin/spec.vim
#cp -f %{SOURCE18} %{buildroot}/%{_datadir}/%{name}/%{vimdir}/syntax/spec.vim

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
cat > $RPM_BUILD_ROOT%{_datadir}/metainfo/gvim.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: Bram@moolenaar.net>
SentUpstream: 2014-05-22
-->
<application>
  <id type="desktop">gvim.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>Vim</project_license>
  <description>
    <p>
     Vim is an advanced text editor that seeks to provide the power of the
     de-facto Unix editor 'Vi', with a more complete feature set.
     It's useful whether you're already using vi or using a different editor.
    </p>
    <p>
     Vim is a highly configurable text editor built to enable efficient text
     editing.
     Vim is often called a "programmer's editor," and so useful for programming
     that many consider it an entire IDE. It is not just for programmers, though.
     Vim is perfect for all kinds of text editing, from composing email to
     editing configuration files.
    </p>
  </description>
  <screenshots>
    <screenshot type="default">
      <image>https://raw.githubusercontent.com/zdohnal/vim/zdohnal-screenshot/gvim16_9.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">http://www.vim.org/</url>
</application>
EOF

( cd %{buildroot}
  ln -sf vi ./%{_bindir}/rvi
  ln -sf vi ./%{_bindir}/rview
  ln -sf vi ./%{_bindir}/view
  ln -sf vi ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,%{buildroot},," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  cp -p .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vi.1
  ln -sf vi.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf gvim ./%{_bindir}/vimx
  %if "%{desktop_file}" == "1"
    desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/gvim.desktop
        # --add-category "Development;TextEditor;X-Red-Hat-Base" D\
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{buildroot}/%{_datadir}/applications/gvim.desktop ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

#appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

# Don't convert, iconv issues with UTF8 a.t.m.
OLDPWD=`pwd`
cd %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF-8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF-8 tutor.it > conv/tutor.it
   #iconv -f CP1253 -t UTF-8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF-8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF-8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF-8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF-8 tutor.gr.cp737 > conv/tutor.gr.cp737
   iconv -f EUC-JP -t UTF-8 tutor.ja.euc > conv/tutor.ja.euc
   iconv -f SJIS -t UTF-8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF-8 -t UTF-8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF-8 -t UTF-8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF-8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF-8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF-8 tutor.sk > conv/tutor.sk
   #iconv -f KOI8R -t UTF-8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF-8 tutor.sv > conv/tutor.sv
   mv -f tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc tutor.sr.cp1250 tutor.sr.utf-8 conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
cd $OLDPWD

# Dependency cleanups
chmod 644 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/profile.d/vim.sh
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/profile.d/vim.csh
chmod 0644 %{buildroot}/%{_sysconfdir}/profile.d/vim.*
install -p -m644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/virc
install -p -m644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/vimrc

# if Vim isn't built for Fedora, use redhat augroup
#%if 0%{?rhel} >= 7
#sed -i -e "s/augroup fedora/augroup redhat/" %{buildroot}/%{_sysconfdir}/vimrc
#sed -i -e "s/augroup fedora/augroup redhat/" %{buildroot}/%{_sysconfdir}/virc
#%endif

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m644 %{SOURCE15} %{buildroot}%{_rpmconfigdir}/macros.d/

(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/tools
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd %{buildroot}/%{_mandir}
  for i in `find ??/ -type f`; do
    if [[ "`file --mime $i`" == *charset=utf-8* ]]; then
      continue
    fi
    bi=`basename $i`
    iconv -f latin1 -t UTF-8 $i > %{buildroot}/$bi
    mv -f %{buildroot}/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1 da.ISO8859-1 de.ISO8859-1; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# use common man1/ru directory
mv %{buildroot}/%{_mandir}/ru.UTF-8 %{buildroot}/%{_mandir}/ru

# Remove duplicate man pages
for i in da.UTF-8 de.UTF-8 fr.UTF-8 it.UTF-8 pl.UTF-8 da.ISO8859-1 de.ISO8859-1 fr.ISO8859-1 it.ISO8859-1 pl.ISO8859-2 ru.KOI8-R; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# Remove unused desktop bits
rm -f %{buildroot}%{_datadir}/applications/gvim.desktop
rm -f %{buildroot}%{_datadir}/applications/vim.desktop
rm -f %{buildroot}%{_datadir}/metainfo/gvim.appdata.xml

for i in rvim.1 gvim.1 gex.1 gview.1 vimx.1; do 
  echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/$i
done
echo ".so man1/vimdiff.1" > %{buildroot}/%{_mandir}/man1/gvimdiff.1
echo ".so man1/vimtutor.1" > %{buildroot}/%{_mandir}/man1/gvimtutor.1
mkdir -p %{buildroot}/%{_mandir}/man5
echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man5/vimrc.5
echo ".so man1/vi.1" > %{buildroot}/%{_mandir}/man5/virc.5
touch %{buildroot}/%{_datadir}/%{name}/vimfiles/doc/tags

# Refresh documentation helptags
%transfiletriggerin common -- %{_datadir}/%{name}/vimfiles/doc
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :

%transfiletriggerpostun common -- %{_datadir}/%{name}/vimfiles/doc
> %{_datadir}/%{name}/vimfiles/doc/tags || :
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :

%files common
%config(noreplace) %{_sysconfdir}/vimrc
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README*
%doc runtime/docs
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vimfiles/template.spec
%dir %{_datadir}/%{name}/%{vimdir}
%{_datadir}/%{name}/%{vimdir}/rgb.txt
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/pack
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%if ! %{withvimspell}
%{_datadir}/%{name}/%{vimdir}/spell
%endif
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(cs.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/cs.cp1250
%lang(da) %{_datadir}/%{name}/%{vimdir}/lang/da
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ja.euc-jp) %{_datadir}/%{name}/%{vimdir}/lang/ja.euc-jp
%lang(ja.sjis) %{_datadir}/%{name}/%{vimdir}/lang/ja.sjis
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(lv) %{_datadir}/%{name}/%{vimdir}/lang/lv
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(nl) %{_datadir}/%{name}/%{vimdir}/lang/nl
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pl.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/pl.UTF-8
%lang(pl.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/pl.cp1250
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(ru.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/ru.cp1251
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sk.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/sk.cp1250
%lang(sr) %{_datadir}/%{name}/%{vimdir}/lang/sr
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(uk.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/uk.cp1251
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_CN.cp936) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.cp936
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/gex.*
%{_mandir}/man1/gview.*
%{_mandir}/man1/gvim*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man1/vimx.*
%{_mandir}/man1/xxd.*
%{_mandir}/man5/vimrc.*
%lang(fr) %{_mandir}/fr/man1/*
%lang(da) %{_mandir}/da/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*

%if %{withvimspell}
%files spell
%dir %{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/vim70/spell/cleanadd.vim
%lang(af) %{_datadir}/%{name}/%{vimdir}/spell/af.*
%lang(am) %{_datadir}/%{name}/%{vimdir}/spell/am.*
%lang(bg) %{_datadir}/%{name}/%{vimdir}/spell/bg.*
%lang(ca) %{_datadir}/%{name}/%{vimdir}/spell/ca.*
%lang(cs) %{_datadir}/%{name}/%{vimdir}/spell/cs.*
%lang(cy) %{_datadir}/%{name}/%{vimdir}/spell/cy.*
%lang(da) %{_datadir}/%{name}/%{vimdir}/spell/da.*
%lang(de) %{_datadir}/%{name}/%{vimdir}/spell/de.*
%lang(el) %{_datadir}/%{name}/%{vimdir}/spell/el.*
%lang(en) %{_datadir}/%{name}/%{vimdir}/spell/en.*
%lang(eo) %{_datadir}/%{name}/%{vimdir}/spell/eo.*
%lang(es) %{_datadir}/%{name}/%{vimdir}/spell/es.*
%lang(fo) %{_datadir}/%{name}/%{vimdir}/spell/fo.*
%lang(fr) %{_datadir}/%{name}/%{vimdir}/spell/fr.*
%lang(ga) %{_datadir}/%{name}/%{vimdir}/spell/ga.*
%lang(gd) %{_datadir}/%{name}/%{vimdir}/spell/gd.*
%lang(gl) %{_datadir}/%{name}/%{vimdir}/spell/gl.*
%lang(he) %{_datadir}/%{name}/%{vimdir}/spell/he.*
%lang(hr) %{_datadir}/%{name}/%{vimdir}/spell/hr.*
%lang(hu) %{_datadir}/%{name}/%{vimdir}/spell/hu.*
%lang(id) %{_datadir}/%{name}/%{vimdir}/spell/id.*
%lang(it) %{_datadir}/%{name}/%{vimdir}/spell/it.*
%lang(ku) %{_datadir}/%{name}/%{vimdir}/spell/ku.*
%lang(la) %{_datadir}/%{name}/%{vimdir}/spell/la.*
%lang(lt) %{_datadir}/%{name}/%{vimdir}/spell/lt.*
%lang(lv) %{_datadir}/%{name}/%{vimdir}/spell/lv.*
%lang(mg) %{_datadir}/%{name}/%{vimdir}/spell/mg.*
%lang(mi) %{_datadir}/%{name}/%{vimdir}/spell/mi.*
%lang(ms) %{_datadir}/%{name}/%{vimdir}/spell/ms.*
%lang(nb) %{_datadir}/%{name}/%{vimdir}/spell/nb.*
%lang(nl) %{_datadir}/%{name}/%{vimdir}/spell/nl.*
%lang(nn) %{_datadir}/%{name}/%{vimdir}/spell/nn.*
%lang(ny) %{_datadir}/%{name}/%{vimdir}/spell/ny.*
%lang(pl) %{_datadir}/%{name}/%{vimdir}/spell/pl.*
%lang(pt) %{_datadir}/%{name}/%{vimdir}/spell/pt.*
%lang(ro) %{_datadir}/%{name}/%{vimdir}/spell/ro.*
%lang(ru) %{_datadir}/%{name}/%{vimdir}/spell/ru.*
%lang(rw) %{_datadir}/%{name}/%{vimdir}/spell/rw.*
%lang(sk) %{_datadir}/%{name}/%{vimdir}/spell/sk.*
%lang(sl) %{_datadir}/%{name}/%{vimdir}/spell/sl.*
%lang(sr) %{_datadir}/%{name}/%{vimdir}/spell/sr.*
%lang(sv) %{_datadir}/%{name}/%{vimdir}/spell/sv.*
%lang(sw) %{_datadir}/%{name}/%{vimdir}/spell/sw.*
%lang(tet) %{_datadir}/%{name}/%{vimdir}/spell/tet.*
%lang(th) %{_datadir}/%{name}/%{vimdir}/spell/th.*
%lang(tl) %{_datadir}/%{name}/%{vimdir}/spell/tl.*
%lang(tn) %{_datadir}/%{name}/%{vimdir}/spell/tn.*
%lang(uk) %{_datadir}/%{name}/%{vimdir}/spell/uk.*
%lang(yi) %{_datadir}/%{name}/%{vimdir}/spell/yi.*
%lang(yi-tr) %{_datadir}/%{name}/%{vimdir}/spell/yi-tr.*
%lang(zu) %{_datadir}/%{name}/%{vimdir}/spell/zu.*
%endif

%files minimal
%config(noreplace) %{_sysconfdir}/virc
%{_bindir}/ex
%{_bindir}/vi
%{_bindir}/view
%{_bindir}/rvi
%{_bindir}/rview
%{_mandir}/man1/vi.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/view.*
%{_mandir}/man5/virc.*

%files enhanced
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%config(noreplace) %{_sysconfdir}/profile.d/vim.*

%files filesystem
%{_rpmconfigdir}/macros.d/macros.vim
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%ghost %{_datadir}/%{name}/vimfiles/doc/tags
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor

%files X11
%if "%{desktop_file}" == "1"
%{_datadir}/metainfo/*.appdata.xml
/%{_datadir}/applications/*
%exclude /%{_datadir}/applications/vim.desktop
%else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
%endif
%{_bindir}/gvimtutor
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimtutor
%{_bindir}/vimx
%{_bindir}/evim
%{_mandir}/man1/evim.*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/locolor/*/apps/*

%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 2:8.1.2102-4
- Enable our python3

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 2:8.1.2102-3
- Switch over to sgug-rse motif/libX11

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 2:8.1.2102-2
- Put back original iconv processing of docs

* Mon Sep 30 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.2102-1
- patchlevel 2102

* Thu Sep 19 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.2056-1
- patchlevel 2056

* Mon Sep 16 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.2019-2
- enable fips warning

* Tue Sep 10 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.2019-1
- patchlevel 2019

* Fri Sep 06 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1991-2
- add f32 as rawhide and f31 as standalone branch

* Fri Sep 06 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1991-1
- patchlevel 1991

* Tue Sep 03 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1912-3
- 1744956 - vim does not build with python3.8

* Mon Aug 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1912-2
- remove python2 interpreter - python2 will be retired soon.
- use 'file' with '--mime' option - output is more stable

* Fri Aug 23 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1912-1
- patchlevel 1912

* Fri Aug 23 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1890-2
- revert vimx removal

* Tue Aug 20 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1890-1
- patchlevel 1890

* Tue Aug 20 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1790-2
- 1740892 - vimx is symlink to gvim instead of vim

* Fri Aug 02 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1790-1
- patchlevel 1790

* Fri Jul 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1749-1
- patchlevel 1749

* Tue Jul 23 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1713-6
- Provides must be unversioned according FPG

* Mon Jul 22 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1713-5
- remove perl-libs, because they are supplied perl MODULE_COMPAT

* Fri Jul 19 2019 Zdenek Dohnal <zdohnal@redhat.com> - 2:8.1.1713-4
- remove unused patch

# vim:nrformats-=octal
