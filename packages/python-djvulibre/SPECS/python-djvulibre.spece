# This package installs two private shared libraries, so don't Provide them.
%global __provides_exclude_from  ^%{python3_sitearch}/.*\\.so)$
%global pypi_name                python-djvulibre
%global srcname                  djvulibre

Name:     python-%{srcname}
Version:  0.8.5
Release:  1%{?dist}
Summary:  Python support for the DjVu image format
License:  GPLv2
URL:      https://jwilk.net/software/python-djvulibre

Source0: %{pypi_source %pypi_name}

BuildRequires: /usr/bin/pkg-config
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: djvulibre >= 3.5.21
BuildRequires: gcc
BuildRequires: ghostscript
BuildRequires: python3-devel >= 3.0
BuildRequires: python3dist(cython) >= 0.20
BuildRequires: python3dist(nose)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(sphinx)

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.



%package -n python3-%{srcname}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open-source implementation of DjVu.


%package -n python-%{srcname}-doc
Summary:    Documentation for python-djvulibre
BuildArch:  noarch

%description -n python-%{srcname}-doc
Documentation for python-djvulibre.



%prep
%autosetup -n %{pypi_name}-%{version}

# Make sure scripts in the examples directory aren't executable
chmod 0644 examples/*



%build
%py3_build
# Move license file to the root of the source directory, so %%license will find it.
mv  ./doc/COPYING  ./
# Generate the HTML documentation.
PYTHONPATH=${PWD} sphinx-build-3 doc/api html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}



%install
%py3_install



%check
# For these tests, import from PYTHONPATH instead of upstream's `djvu` subdirectory.
rm -rf ./djvu/
PYTHONPATH=%{buildroot}/%{python3_sitearch} nosetests-%{python3_version}



%files -n python3-%{srcname}
%license COPYING
%{python3_sitearch}/djvu/
%{python3_sitearch}/python_djvulibre-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%license COPYING
%doc     html/  examples/



%changelog
* Wed Dec 18 2019 Andrew Toskin <andrew@tosk.in> - 0.8.5-1
- Initial package (starting over from scratch).
