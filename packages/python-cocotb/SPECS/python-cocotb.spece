# Created by pyp2rpm-3.3.2
%global pypi_name cocotb

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        2%{?dist}
Summary:        Coroutine Co-simulation Test Bench

License:        BSD
URL:            https://github.com/cocotb/cocotb
Source0:        https://github.com/cocotb/cocotb/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  gcc, gcc-c++, make

# iverilog and ghdl are the FOSS simulators. cocotb supports both.
# We need them to run the tests.
BuildRequires:  iverilog, ghdl

# So this package doesn't actually contain compiled code (at the moment).
# But it does contain source code that users compile when running a
# simulator. So maybe arguably it should be arched.
# Future versions of cocotb may contain the option to have precompiled
# libraries.
BuildArch:      noarch

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Provide "cocotb", as that's the upstream name and this is
# a framework end-users would use directly.
Provides:       cocotb = %{version}-%{release}

# It isn't *strictly* necessary to have iverilog/ghdl installed, especially
# since cocotb also supports non-FOSS simulators. Thus, use a weak dep to
# pull them in (but allow someone to remove them if necessary).
Recommends:     iverilog, ghdl

%description
cocotb is a coroutine based cosimulation library for writing VHDL
and Verilog testbenches in Python.

%description -n python3-%{pypi_name}
cocotb is a coroutine based cosimulation library for writing VHDL
and Verilog testbenches in Python.

%prep
%autosetup -n %{pypi_name}-%{version}

# Only run the tests, not the examples.
# Examples require /usr/bin/cocotb-config already installed.
sed "/\$(MAKE) -k -C examples/d" -i Makefile

# Fix the 'combine_results.py' script to use python3.
sed 's/env python/python3/g' -i bin/combine_results.py

# Should remove chbangs from non-script library files.
sed "/env python/d" -i cocotb/*.py
sed "/env python/d" -i cocotb/drivers/*.py
sed "/env python/d" -i cocotb/generators/*.py
sed "/env python/d" -i cocotb/monitors/*.py

# PyEval_InitThreads() is deprecated in 3.9.
sed "/PyEval_InitThreads/d" -i cocotb/share/lib/embed/gpi_embed.c

# This is deprecated in 3.9 too.
sed "s/cElementTree/ElementTree/g" -i bin/combine_results.py

%build
%py3_build

%install
%py3_install

%check
# Run tests with the FOSS simulators.
export PYTHON_BIN=python3
make SIM=icarus

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/cocotb-config
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.1-1
- Update to latest upstream release.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.0-1
- Update to latest upstream release.

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-3
- Move Recommends on iverilog/ghdl into python3 subpackage.

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-2
- Rename package to 'python-cocotb', provide 'cocotb'.
- Remove unnecessary manual dependency on setuptools.
- Remove unnecessary removal of egg info file.
- Change combine_results script to not use "env" to find python3 interpreter
- Change egg info file in files list to use '*' instead of '?' pattern matching.

* Fri Jul 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-1
- Initial package.
