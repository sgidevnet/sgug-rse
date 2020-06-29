# Multiple tests currently failing. In touch with upstream about these. They're
# looking into it, but it'll take time for them to fix them all. Suggested we
# disable tests for the time being.
# https://github.com/SmokinCaterpillar/pypet/issues/57
%bcond_without tests

%global pypi_name pypet

%global _description %{expand:
The new python parameter exploration toolkit: pypet manages exploration of the
parameter space of any numerical simulation in python, thereby storing your
data into HDF5 files for you. Moreover, pypet offers a new data container which
lets you access all your parameters and results from a single source. Data I/O
of your simulations and analyses becomes a piece of cake!}

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        2%{?dist}
Summary:        Parameter exploration toolbox

License:        BSD
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        https://github.com/SmokinCaterpillar/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For tests
%if %{with tests}
BuildRequires:  %{py3_dist brian2}
BuildRequires:  %{py3_dist deap}
BuildRequires:  hdf5
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist tables}
%endif

# For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(amsthm.sty)
BuildRequires:  /usr/bin/dvipng

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Update sphinx.ext.pngmath -> imgmath
sed -i 's/sphinx.ext.pngmath/sphinx.ext.imgmath/' doc/source/conf.py

# Remove gitignore files
rm -fv  examples/{,example_17_wrapping_an_existing_project,example_24_large_scale_brian2_simulation}/.gitignore

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

make -C doc SPHINXBUILD=sphinx-build-3 html
rm -rf doc/build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

%check
# https://github.com/SmokinCaterpillar/pypet/blob/develop/ciscripts/travis/runtests.sh
# Scoop is unmaintained. I've asked upstream to drop support for it:
# https://github.com/SmokinCaterpillar/pypet/issues/56
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} pypet/tests/all_single_core_tests.py
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%files doc
%license LICENSE CHANGES.txt
%doc doc/build/html examples/

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-2
- Explicitly BR setuptools

* Tue Jun 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.0-1
- Update to 0.5.0
- Enable tests

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-1
- Add missing BRs for docs

* Fri May 22 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.3-1
- Initial spec
