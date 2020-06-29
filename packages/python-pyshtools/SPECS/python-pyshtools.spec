%global srcname pyshtools

Name:           python-%{srcname}
Version:        4.6.2
Release:        2%{?dist}
Summary:        Tools for working with spherical harmonics

License:        BSD
URL:            https://shtools.github.io/SHTOOLS/
Source0:        %pypi_source

BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  fftw3-devel
BuildRequires:  openblas-devel

%description
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(astropy)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy) >= 0.14
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(xarray)

%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
pysthools is a Python library that can be used to perform spherical
harmonic transforms and reconstructions, multitaper spectral analyses on
the sphere, expansions of functions into Slepian bases, and standard
operations on global gravitational and magnetic field data.


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

# Remove extra files
rm -r examples/notebooks/.ipynb_checkpoints

# Don't make f2py silent.
sed -i -e '/f2py_options/d' setup.py


%build
%py3_build


%install
%py3_install


%check
#{python3} examples/notebooks/test_notebooks.py
export MPLBACKEND=Agg
export PYTHONPATH=%{buildroot}%{python3_sitearch}
make -C examples/python -f Makefile no-timing PYTHON=%{python3}


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.2-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.6.2-1
- Update to latest version
- Cleanup old workarounds

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.5-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.4.1-1
- Update to latest version

* Sat Aug 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3-1
- Initial package.
