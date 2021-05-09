Name:           pdfposter
Version:        0.7.post1
Release:        3%{?dist}
Summary:        Scale and tile PDF images/pages to print on multiple pages

License:        GPLv3+
URL:            https://pdfposter.readthedocs.io
Source0:        %pypi_source pdftools.pdfposter

BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       python3-PyPDF2

%description
Pdfposter can be used to create a large poster by building it from multple
pages and/or printing it on large media. It expects as input a PDF file,
normally printing on a single page. The output is again a PDF file, maybe
containing multiple pages together building the poster.  The input page 
will be scaled to obtain the desired size.

%prep
%setup -q -n pdftools.%{name}-%{version}
# Remove shebang
for Files in pdftools/pdfposter/cmd.py pdftools/pdfposter/__init__.py; do
  sed -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  rm ${Files}.orig
done

%build
%py3_build

%install
%py3_install

%files
%doc README.txt
%{_bindir}/%{name}
%{python3_sitelib}/pdftools/
%{python3_sitelib}/pdftools.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.post1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.post1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.post-1
- Updated to new upstream version 0.7.post1 (rhbz#1645691)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Spec file updated
- Updated to new upstream version 0.6.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-10
- Updated python BR

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-8
- Added missing file

* Fri Aug 12 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-7
- Rebuild (pypdf)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Feb 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-4
- Updated BR

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Replaced 'define' with 'global'

* Sun May 03 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Updated to new upstream version 0.5.0

* Thu Apr 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-1
- Initial package for Fedora
