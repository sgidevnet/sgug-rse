# Created by pyp2rpm-2.0.0, then modified.
%global pypi_name pdfminer.six

Name:           python-pdfminer
Version:        20181108
Release:        7%{?dist}
Summary:        PDF parser and analyzer

License:        MIT
URL:            https://github.com/goulu/pdfminer

Source0:        https://github.com/pdfminer/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Fedora's pycryptodomex is renamed to not conflict with pycrypto.
Patch0001:      Use-Fedora-pycryptodomex.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Require the separately packaged CMAP resources.
BuildRequires:  cmap-resources-japan1-6, cmap-resources-korea1-2, cmap-resources-gb1-5, cmap-resources-cns1-7

# Helper tools and dependencies.
BuildRequires: python3-six
BuildRequires: python3-chardet
BuildRequires: python3-pycryptodomex
BuildRequires: python3-sortedcontainers
BuildRequires: python3-nose

%description
PDFMiner is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting and
analyzing text data. PDFMiner allows to obtain the exact location
of texts in a page, as well as other information such as fonts or
lines. It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible PDF
parser that can be used for other purposes instead of text analysis.

This is actually pdfminer.six, a backwards-compatible fork of
PDFMiner using six for Python 2+3 compatibility.


%package -n     python3-pdfminer
Summary:        PDF parser and analyzer

# In case anyone installed pdfminer-six from the copr, replace it.
Obsoletes: python3-pdfminer-six < 20151013-4.fc23
Provides:  python3-pdfminer-six = %{version}-%{release}

# Since the unversioned programs changed subpackages.
Conflicts: python2-pdfminer < 20181108-1.fc30

%{?python_provide:%python_provide python3-pdfminer}

%description -n python3-pdfminer

PDFMiner is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting and
analyzing text data. PDFMiner allows to obtain the exact location
of texts in a page, as well as other information such as fonts or
lines. It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible PDF
parser that can be used for other purposes instead of text analysis.

This is actually pdfminer.six, a backwards-compatible fork of
PDFMiner using six for Python 2+3 compatibility.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the bundled cmap data and replace it with that provided by the package
rm cmaprsrc/*
rm pdfminer/cmap/*
cp %{_datadir}/cmap/cmap-japan1-7/cid2code.txt cmaprsrc/cid2code_Adobe_Japan1.txt
cp %{_datadir}/cmap/cmap-korea1-2/cid2code.txt cmaprsrc/cid2code_Adobe_Korea1.txt
cp %{_datadir}/cmap/cmap-gb1-5/cid2code.txt cmaprsrc/cid2code_Adobe_GB1.txt
cp %{_datadir}/cmap/cmap-cns1-7/cid2code.txt cmaprsrc/cid2code_Adobe_CNS1.txt

# A single file has a 'python' shebang in it, fix that so later assumptions work.
sed -i '/^#!\//, 1d' pdfminer/psparser.py

# 'make cmap' uses "python". Make it use "python3".
sed 's/PYTHON=python/PYTHON?=python3/g' -i Makefile


%build
# Make the cmap resources.
make cmap

%py3_build


%install
# Also, ship symlinks of the scripts without the .py syntax.

%py3_install
sed 's/python2 -s/python3 -s/' -i %{buildroot}/%{_bindir}/*.py
ln -sf %{_bindir}/pdf2txt.py %{buildroot}/%{_bindir}/pdf2txt
ln -sf %{_bindir}/dumppdf.py %{buildroot}/%{_bindir}/dumppdf
ln -sf %{_bindir}/latin2ascii.py %{buildroot}/%{_bindir}/latin2ascii


%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} \
    nosetests-3


%files -n python3-pdfminer
%{_bindir}/pdf2txt
%{_bindir}/pdf2txt.py
%{_bindir}/dumppdf
%{_bindir}/dumppdf.py
%{_bindir}/latin2ascii
%{_bindir}/latin2ascii.py
%{python3_sitelib}/pdfminer
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%doc docs/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20181108-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20181108-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20181108-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20181108-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 20181108-1
- Update to latest version
- Enable tests
- Fix crypto dependency
- Switch to automatic Requires
- Drop Python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170720-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Ben Rosser <rosser.bjr@gmail.com> - 20170720-7
- Stop package from using 'python' to run cmap script.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20170720-6
- Rebuilt for Python 3.7

* Tue May 22 2018 Ben Rosser <rosser.bjr@gmail.com> - 20170720-5
- Rebuild against new cmap resources package.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170720-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20170720-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170720-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170720-1
- Update to latest upstream release.

* Fri Apr 21 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170419-1
- Update to latest upstream release, fixing a logging bug from 20170418.

* Fri Apr 21 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170418-2
- Now that upstream patch removing chbangs was merged, don't chmod library files.

* Wed Apr 19 2017 Ben Rosser <rosser.bjr@gmail.com> - 20170418-1
- Updated to latest upstream release.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160614-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 20160614-6
- Rebuild for Python 3.6

* Sat Oct 22 2016 Ben Rosser <rosser.bjr@gmail.com> - 20160614-5
- Add missing requires on python-six and python-chardet.

* Fri Sep  9 2016 Ben Rosser <rosser.bjr@gmail.com> - 20160614-4
- Rebuild against latest cmap-resources.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160614-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 21 2016 Ben Rosser <rosser.bjr@gmail.com> 20160614-2
- I forgot to actually apply the patch to remove chbangs from library files. Apply said patch.

* Tue Jun 14 2016 Ben Rosser <rosser.bjr@gmail.com> 20160614-1
- Update to latest upstream version of package.
- Use local version of patch.

* Sat Feb 27 2016 Ben Rosser <rosser.bjr@gmail.com> 20160202-3
- Added a patch to remove the chbangs from all library files.
- Write correct sed command to make python3 scripts run with python3.

* Sat Feb 27 2016 Ben Rosser <rosser.bjr@gmail.com> 20160202-2
- Through the use of some gratuitious sed, the python2 package only depends on /usr/bin/python2.
- The python3 version is still a little weird; it pulls in /usr/bin/python and I'm not sure why.
- Also, make the python 3 scripts be the default ones.

* Fri Feb 26 2016 Ben Rosser <rosser.bjr@gmail.com> 20160202-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 1 2016 Ben Rosser <rosser.bjr@gmail.com> 20151013-5
- Version bump to silence rpmlint.

* Fri Jan 1 2016 Ben Rosser <rosser.bjr@gmail.com> 20151013-4
- Upgrade path; obsolete and provide the pdfminer-six package in the COPR.
- Now replace the original python-pdfminer package with this one.

* Fri Jan 1 2016 Ben Rosser <rosser.bjr@gmail.com> 20151013-3
- Upgrade path; obsolete and provide python-pdfminer up until rawhide.

* Sat Dec 19 2015 Ben Rosser <rosser.bjr@gmail.com> 20151013-2
- Ship symlinks of the pdfminer scripts without the .py suffix.

* Fri Dec 18 2015 Ben Rosser <rosser.bjr@gmail.com> - 20151013-1
- Initial package of the pdfminer.six fork using pyp2rpm.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140328-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 23 2014 Ben Rosser <rosser.bjr@gmail.com> 20140328-2
- Replaced /usr/bin with bindir macro in install section.

* Sat Aug 16 2014 Ben Rosser <rosser.bjr@gmail.com> 20140328-1
- Updated to latest version of pdfminer.
- Changed specfile to depend on the correct cmap-* packages.

* Thu Sep 20 2012 Ben Rosser <rosser.bjr@gmail.com> 20110515-4
- Removed bundled cmap, changed to depend on cmap package instead

* Thu Jul 05 2012 Ben Rosser <rosser.bjr@gmail.com> 20110515-3
- Removed BuildRoot, clean, and first line of install
- Fixed issue with cmap data not being copied into package
- Fixed license (cmap is under BSD, not MIT)

* Tue May 22 2012 Ben Rosser <rosser.bjr@gmail.com> 20110515-2
- Fixed unowned directory issue and cleaned up the spec file

* Fri May 18 2012 Ben Rosser <rosser.bjr@gmail.com> 20110515-1
- Initial version of the package

