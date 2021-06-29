# On every new version, we need to do a local build to make
# the PDF docs, and update the source files in CVS.
%global makedocs 0

Name:          lout
Summary:       A document formatting system
Version:       3.40
Release:       15%{?dist}
License:       GPLv2+
URL:           http://savannah.nongnu.org/projects/lout/
Source0:       http://download.savannah.gnu.org/releases/lout/lout-%{version}.tar.gz
%if !%{makedocs}
Source1:       design.pdf
Source2:       expert-guide.pdf
Source3:       user-guide.pdf
Source4:       slides.pdf
%endif
Patch0:        makefile.patch
Patch1:        fix-FSF-address.patch
BuildRequires: ghostscript, gcc

%description
Lout is a document formatting system designed and implemented by Jeffrey
Kingston at the Basser Department of Computer Science, University of
Sydney, Australia. The system reads a high-level description of a document
similar in style to LaTeX and produces a PostScript file which can be
printed on most laser printers and graphic display devices. Plain text
output is also available, PDF output is limited but working (e.g. no
graphics). Lout is inherently multilingual. Adding new languages is easy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make COPTS="$RPM_OPT_FLAGS" \
     BINDIR=%{_bindir} \
     LOUTLIBDIR=%{_datadir}/%{name} \
     LOUTDOCDIR=%{_datadir}/%{name}/doc \
     MANDIR=%{_mandir}/man1 \
     prg2lout lout

function render_docs {
    subdir=$1
    pdf_file=$2
    passes=$3

    curdir=$(pwd)
    pushd doc/$subdir

    # We need to set the PATH variable here, because lout eventually exec's
    #   prg2lout.  In order for lout to find the latter, we have to set the
    #   PATH.
    # We also need to tell lout where to find its files, since we haven't
    #   installed them in their final location under /usr/share/lout/ yet.
    PATH=$curdir lout \
       -I $curdir/include \
       -D $curdir/data \
       -F $curdir/font \
       -H $curdir/hyph \
       -C $curdir/maps \
       -r${passes} all > outfile.ps
    # Note that the above clobbers the prebuilt file outfile.ps that is
    # included in Lout's source tarball.
    ps2pdf outfile.ps ../${pdf_file}
    rm *.li *.ld outfile.ps
    popd
}

# For some reason, ps2pdf segfaults in koji.
%if %{makedocs}
render_docs design design.pdf       3
render_docs expert expert-guide.pdf 4
render_docs slides slides.pdf       2
render_docs user   user-guide.pdf   6
%else
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} doc/
%endif

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/doc
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
     LOUTLIBDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
     LOUTDOCDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
     MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
     install installman installdoc

# Looks like vim dump? Doesn't happen anymore. Weird.
# rm -rvf $RPM_BUILD_ROOT%%{_datadir}/%%{name}/doc/user/.pie_intr.swp

%files
%doc README READMEPDF
%license COPYING
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/*.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 3.40-12
- Fix rpmlint issues.

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 3.40-11
- Add BuildRequires gcc per new PG.
- Fix FSF addresses (actually, remove them as the upstream does).

* Thu Feb 08 2018 Matěj Cepl <mcepl@redhat.com> - 3.40-10
- Remove Group, it has been unnecessary since RHEL-6.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Matěj Cepl <mcepl@redhat.com> - 3.40-5
- Update to all supported branches.
- Comment out weird removal of .pie_intr.swp file.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 3.40-3
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 12 2015 Matej Cepl <mcepl@redhat.com> - 3.40-1
- New upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.38-1
- 3.38

* Thu Oct 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.37-4
- enable makedocs

* Thu Oct  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.37-3
- don't build the docs in koji due to random ps2pdf segfault

* Wed Oct  1 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.37-2
- try using ps2pdf

* Wed Oct  1 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.37-1
- update to 3.37

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.36-2
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.36-1
- Update to lout-3.36.  Render PDF versions of the Lout documentation.
  Thanks to Vadim Nasardinov <vnasardinov@gmail.com> for the fixes.

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-7
- fix license (GPLv2+), rebuild in devel for BuildID

* Tue Sep 12 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-6
- bump for FC-6

* Fri Jul  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-5
- revive package

* Fri Jul  1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-4
- delete hidden trash file

* Thu Jun 30 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-3
- cleanups, macro consistency

* Thu Jun 30 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-2
- remove hardcoded directory definitions
- link with shared zlib, not static

* Thu Jun 30 2005 Tom "spot" Callaway <tcallawa@redhat.com> 3.30-1
- initial package for Fedora Extras
