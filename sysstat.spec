#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysstat
Version  : 11.3.3
Release  : 20
URL      : http://pagesperso-orange.fr/sebastien.godard/sysstat-11.3.3.tar.bz2
Source0  : http://pagesperso-orange.fr/sebastien.godard/sysstat-11.3.3.tar.bz2
Summary  : SAR, SADF, MPSTAT, IOSTAT, TAPESTAT, PIDSTAT and CIFSIOSTAT for Linux
Group    : Development/Tools
License  : GPL-2.0
Requires: sysstat-bin
Requires: sysstat-doc
Requires: sysstat-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd
BuildRequires : systemd-dev
Patch1: stateless.patch

%description
The sysstat package contains the sar, sadf, mpstat, iostat, tapestat,
pidstat, cifsiostat and sa tools for Linux.
The sar command collects and reports system activity information.
The information collected by sar can be saved in a file in a binary
format for future inspection. The statistics reported by sar concern
I/O transfer rates, paging activity, process-related activities,
interrupts, network activity, memory and swap space utilization, CPU
utilization, kernel activities and TTY statistics, among others. Both
UP and SMP machines are fully supported.
The sadf command may  be used to display data collected by sar in
various formats (CSV, XML, etc.) and to draw graphs (SVG).
The iostat command reports CPU utilization and I/O statistics for disks.
The tapestat command reports statistics for tapes connected to the system.
The mpstat command reports global and per-processor statistics.
The pidstat command reports statistics for Linux tasks (processes).
The cifsiostat command reports I/O statistics for CIFS filesystems.

%package bin
Summary: bin components for the sysstat package.
Group: Binaries

%description bin
bin components for the sysstat package.


%package doc
Summary: doc components for the sysstat package.
Group: Documentation

%description doc
doc components for the sysstat package.


%package locales
Summary: locales components for the sysstat package.
Group: Default

%description locales
locales components for the sysstat package.


%prep
cd ..
%setup -q -n sysstat-11.3.3
%patch1 -p1

%build
%reconfigure --disable-static --disable-sensors \
--enable-nls \
--disable-file-attr \
--disable-install-cron \
--disable-stripping
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
%find_lang sysstat

%files
%defattr(-,root,root,-)
/usr/lib64/sa/sa1
/usr/lib64/sa/sa2
/usr/lib64/sa/sadc
/usr/lib64/sa/sysstat.ioconf

%files bin
%defattr(-,root,root,-)
/usr/bin/cifsiostat
/usr/bin/iostat
/usr/bin/mpstat
/usr/bin/pidstat
/usr/bin/sadf
/usr/bin/sar
/usr/bin/tapestat

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/sysstat/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files locales -f sysstat.lang 
%defattr(-,root,root,-)

