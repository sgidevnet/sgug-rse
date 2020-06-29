# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
%if 0%{?fedora} < 30
%global with_py2 1
%else
%global with_py2 0
%endif

%global srcname  neo

%global _description %{expand: \
Neo is a package for representing electrophysiology data in Python, together
with support for reading a wide range of neurophysiology file formats,
including Spike2, NeuroExplorer, AlphaOmega, Axon, Blackrock, Plexon, Tdt, and
support for writing to a subset of these formats plus non-proprietary formats
including HDF5.

The goal of Neo is to improve interoperability between Python tools for
analyzing, visualizing and generating electrophysiology data (such as
OpenElectrophy, NeuroTools, G-node, Helmholtz, PyNN) by providing a common,
shared object model. In order to be as lightweight a dependency as possible,
Neo is deliberately limited to represention of data, with no functions for data
analysis or visualization.

Neo implements a hierarchical data model well adapted to intracellular and
extracellular electrophysiology and EEG data with support for multi-electrodes
(for example tetrodes). Neos data objects build on the quantities_ package,
which in turn builds on NumPy by adding support for physical dimensions. Thus
neo objects behave just like normal NumPy arrays, but with additional metadata,
checks for dimensional consistency and automatic unit conversion.

Read the documentation at http://neo.readthedocs.io/}

Name:       python-%{srcname}
Version:    0.8.0
Release:    3%{?dist}
Summary:    Represent electrophysiology data in Python

License:    BSD
URL:        http://neuralensemble.org/%{srcname}/
Source0:    https://github.com/neuralensemble/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist quantities}
BuildRequires:  %{py3_dist coverage}
BuildRequires:  %{py3_dist tox}

# Basic requires picked up by autogenerator

# Extra requires:
# Not in fedora yet, to be updated as these are added
# Recommends:  %%{py3_dist stfio}
Recommends:  %{py3_dist nixio}
Recommends:  %{py3_dist klusta}
Recommends:  %{py3_dist scipy}
Recommends:  %{py3_dist hypy}
Recommends:  %{py3_dist igor}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%if %{?with_py2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  %{py2_dist setuptools}
BuildRequires:  %{py2_dist nose}
BuildRequires:  %{py2_dist numpy}
BuildRequires:  %{py2_dist quantities}
BuildRequires:  %{py3_dist coverage}
# Basic requires picked up by autogenerator

# Extra requires:
# Not in fedora yet, to be updated as these are added
# Recommends:  %%{py2_dist stfio}
Recommends:  %{py2_dist nixio}
Recommends:  %{py2_dist klusta}
Recommends:  %{py2_dist scipy}
Recommends:  %{py2_dist hypy}
Recommends:  %{py2_dist igor}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{_description}
%endif

%prep
%autosetup
# stray backup file?
rm -fv neo/io/nwbio_BACKUP_4246.py
rm -rf neo.egg-info

%build
%if %{?with_py2}
%py2_build
%endif
%py3_build

%install
%if %{?with_py2}
%py2_install
%endif
%py3_install

%check
# All excluded tests need internet connection for downloading data files
%if %{?with_py2}
nosetests-%{python2_version} -vx --exclude=iotest --exclude=rawio
%endif
nosetests-%{python3_version} -vx --exclude=iotest --exclude=rawio

%if %{?with_py2}
%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst examples doc/source/authors.rst CODE_OF_CONDUCT.md CITATION.txt
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{srcname}/
%endif

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst examples doc/source/authors.rst CODE_OF_CONDUCT.md CITATION.txt
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update to 0.8.0
- Add packaged recommends

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-0.3.20190215git49b6041
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.2.20190215git49b6041
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.8.0-0.1.20190215git49b6041
- Pre-release 0.8.0
- Tests activated

* Wed Feb 06 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.7.1-1
- Release 0.7.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-6
- Cosmetic improvements
- Re-add py2 subpackage but disable from F30+

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.1-5
- Subpackage python2-neo has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-2
- Use python dist macros
- Use github source

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.1-1
- Update to latest upstream release
- Remove doc subpackage. Use readthedocs instead.
- Skip tests, they fetch data from the internet

* Sun Jan 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.2-1
- Update to latest upstream release
- update requires and recommends

* Mon Jun 26 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Update to latest upstream release

* Wed Feb 01 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.1-1
- Update to latest upstream release

* Tue Oct 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.3.3-1
- Initial rpmbuild
