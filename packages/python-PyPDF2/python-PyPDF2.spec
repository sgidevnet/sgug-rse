%global srcname PyPDF2
%global with_python3 1
%global sum Python PDF toolkit and library

Name:           python-%{srcname}
Version:        1.26.0
Release:        8%{?dist}
License:        BSD
Summary:        %{sum}
Source:         https://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz
URL:            https://github.com/mstamy2/PyPDF2

BuildArch:      noarch


%description
A pure Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encryption and decryption of PDF files.

By being pure Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  python2-libs
Obsoletes:      python-%{srcname} <= 1.25.1-6
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
A pure Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encryption and decryption of PDF files.

By being pure Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python2-libs
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
A pure Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encryption and decryption of PDF files.

By being pure Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.

%package -n python-%{srcname}-doc
Summary:    Documentation for python-%{srcname}

%description -n python-%{srcname}-doc
python-PyPDF2 contains documentation and examples for the python-PyPDF package

%prep
%autosetup -n %{srcname}-%{version}

# non-executable script
sed -i -e '/^#!\//, 1d' PyPDF2/pagerange.py

# Lots of things in the repo shouldn't be executable
chmod a-x Scripts/* Sample_Code/* LICENSE README.md CHANGELOG


%build
%py2_build
%py3_build


%install
%py3_install
%py2_install


%check
# NOTE: Upstream has some testing bugs
#python -m unittest Tests.tests


%files -n python2-%{srcname}
%{python2_sitelib}/*
%license LICENSE

%files -n python3-%{srcname}
%{python3_sitelib}/*
%license LICENSE

%files -n python-%{srcname}-doc
%doc README.md CHANGELOG Scripts/ Sample_Code/
%license LICENSE

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.26.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.26.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 major <major@mhtx.net> - 1.26.0-1
- Upstream version 1.26.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.25.1-14
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.1-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Major Hayden <major@mhtx.net> - 1.25.1-12
- Setting srcname variable so python_provide works properly
- Removing Provides tag

* Fri May 20 2016 Major Hayden <major@mhtx.net> - 1.25.1-11
- Adding Provides tag to fix dependency problems

* Thu May 19 2016 Major Hayden <major@mhtx.net> - 1.25.1-10
- Correcting python_provides line for python2

* Thu May 19 2016 Major Hayden <major@mhtx.net> - 1.25.1-9
- Removing srcname variable in Provides

* Mon May 16 2016 Major Hayden <major@mhtx.net> - 1.25.1-8
- Correcting typo

* Mon May 16 2016 Major Hayden <major@mhtx.net> - 1.25.1-7
- Adding version number to obsoletes tag

* Thu May 5 2016 Major Hayden <major@mhtx.net> - 1.25.1-6
- Adding obsoletes tag

* Thu May 5 2016 Major Hayden <major@mhtx.net> - 1.25.1-5
- Fixed Python 3 packaging

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 23 2015 Major Hayden <major@mhtx.net> - 1.25.1-2
- Additional package review fixes

* Fri Sep 11 2015 Major Hayden <major@mhtx.net> - 1.25.1-1
- Initial package
