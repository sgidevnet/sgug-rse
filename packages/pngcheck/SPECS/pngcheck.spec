Name:           pngcheck
Version:        2.3.0
Release:        4%{?dist}
Summary:        Verifies the integrity of PNG, JNG and MNG files

# Note that the main package contains only pngcheck, compiled from a single
# source file, pngcheck.c, under a minimal MIT license. The new utilities
# licensed under GPLv2+ are compiled from the gpl/ subdirectory and packaged in
# the extras subpackage.
#
# Per Fedora guidelines, emailed upstream (Greg Roelofs) 2020-10-12 to suggest
# the license text should be in a separate file, not just a source file
# comment, in any future releases. Upstream added license text in 2.4.0.
License:        MIT
URL:            http://www.libpng.org/pub/png/apps/pngcheck.html
Source0:        https://downloads.sourceforge.net/png-mng/%{name}-%{version}.tar.gz

# Minimal patch to ensure all format strings are literals instead of buffers
# (even const buffers) so we can compile with -Werror=format-security. The
# format strings were never modified in practice, so this does not change
# program behavior.
#
# No upstream bug tracker; sent patch upstream via email to Greg Roelofs
# 2020-10-12. Upstream applied patch or equivalent in 2.4.0.
Patch0:         %{name}-format-security.patch
# Fix buffer overflow reported in RHBZ #1897485.
#
# When char is signed, casting to a (signed) int directly could produce a
# negative offset into the ASCII lookup table; adding an intermediate cast to
# uch (a typedef for unsigned char) ensures a nonnegative offset no greater
# than 255, which always corresponds to a valid table index.
Patch1:         %{name}-2.3.0-overflow-bz1897485.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  help2man

# Default on Fedora; still needed for EPEL
%global _hardened_build 1

%description
pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the
internal 32-bit CRCs [checksums] and decompressing the image data); it can
optionally dump almost all of the chunk-level information in the image in
human-readable form. For example, it can be used to print the basic statistics
about an image (dimensions, bit depth, etc.); to list the color and
transparency info in its palette (assuming it has one); or to extract the
embedded text annotations. This is a command-line program with batch
capabilities.

The current release supports all PNG, MNG and JNG chunks, including the newly
approved sTER stereo-layout chunk. It correctly reports errors in all but two
of the images in Chris Nokleberg's brokensuite-20061204.


%package extras
Summary:        Helper utilities distributed with %{name}
License:        GPLv2+

%description extras
Included with pngcheck (since version 2.1.0) are two helper utilities:

  - pngsplit - break a PNG, MNG or JNG image into constituent chunks (numbered
    for easy reassembly)
  - png-fix-IDAT-windowsize - fix minor zlib-header breakage caused by libpng
    1.2.6


%prep
%autosetup -p1


%build
%set_build_flags
%make_build -f Makefile.unx \
    CFLAGS="${CFLAGS-} -DUSE_ZLIB $(pkg-config --cflags zlib)" \
    LIBS="${LDFLAGS-} $(pkg-config --libs zlib)"

# For each built binary:
find . -maxdepth 1 -type f -perm /0111 | while read -r bin
do
  # Generate a man page from the help output:
  help2man \
      --no-discard-stderr \
      --help-option=-h \
      --version-string="$(
        # Get the version number of the particular binary from its help output;
        # replace spaces with hyphens to workaround help2man limitations.
        "./${bin}" -h 2>&1 |
          grep -Eio 'version [^,]+,' |
          sed -r -e 's/^version +//' -e 's/( *of .*)?,$//' -e 's/ /-/g'
      )" \
      --no-info \
      "./${bin}" |
    # Strip information about runtime zlib version in the build environment from
    # the man page, as it may not apply to the installed environment.
    sed -r 's/; using zlib .*/./' > "${bin}.1"
done


%install
install -d '%{buildroot}%{_bindir}'
install -d '%{buildroot}%{_mandir}/man1'
find . -maxdepth 1 -type f -perm /0111 | while read -r bin
do
  install -t '%{buildroot}%{_bindir}' -p "${bin}"
  install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p "${bin}.1"
done


%files
%doc CHANGELOG
%doc README
%{_bindir}/pngcheck
%{_mandir}/man1/pngcheck.1*


%files extras
%license gpl/COPYING
%doc CHANGELOG
%doc README
%{_bindir}/pngsplit
%{_bindir}/png-fix-IDAT-windowsize
%{_mandir}/man1/pngsplit.1*
%{_mandir}/man1/png-fix-IDAT-windowsize.1*


%changelog
* Fri Nov 13 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-4
- Fix buffer overflow (RHBZ #1897485)

* Wed Oct 28 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-3
- Add _hardened_build macro for EPEL

* Wed Oct 28 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-2
- Work around Makefile.unx not actually using LDFLAGS; this fixes hardened
  build (PIE)

* Thu Oct 15 2020 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-1
- Initial import (#1886858)
